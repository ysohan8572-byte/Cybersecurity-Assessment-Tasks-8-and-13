#!/usr/bin/env python3
"""AuthLog Sentinel — defensive analysis of a local CSV sample."""
import argparse
import csv
from collections import Counter
from pathlib import Path

REQUIRED = {"timestamp", "username", "source_ip", "event"}

def analyze(path: Path, threshold: int = 3):
    failures = Counter()
    total = 0
    with path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or not REQUIRED.issubset(reader.fieldnames):
            raise ValueError("CSV must contain: timestamp, username, source_ip, event")
        for row in reader:
            total += 1
            event = (row.get("event") or "").strip().upper()
            user = (row.get("username") or "").strip() or "(missing)"
            ip = (row.get("source_ip") or "").strip() or "(missing)"
            if event == "FAILED":
                failures[(user, ip)] += 1
    alerts = [(user, ip, count) for (user, ip), count in failures.items()
              if count >= threshold]
    alerts.sort(key=lambda item: (-item[2], item[0], item[1]))
    return total, failures, alerts

def main():
    parser = argparse.ArgumentParser(description="Flag repeated failed logins in a CSV file.")
    parser.add_argument("csv_file", type=Path, help="Path to authentication CSV")
    parser.add_argument("--threshold", type=int, default=3,
                        help="Alert at this many failures (default: 3)")
    args = parser.parse_args()
    if args.threshold < 1:
        parser.error("--threshold must be at least 1")
    try:
        total, failures, alerts = analyze(args.csv_file, args.threshold)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(f"Events processed: {total}")
    print(f"Failed-login combinations: {len(failures)}")
    if not alerts:
        print("No combinations met the alert threshold.")
    else:
        print("ALERT: repeated failed logins")
        for user, ip, count in alerts:
            print(f"  username={user} source_ip={ip} failures={count}")
    print("Review alerts with system, time-window, and user context.")

if __name__ == "__main__":
    main()
