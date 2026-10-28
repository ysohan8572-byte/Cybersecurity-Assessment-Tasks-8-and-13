WINDOWS PRACTICAL EVIDENCE KIT
================================

Important:
- Task 13 uses synthetic sample authentication logs. This is a real, reproducible run of the provided local Python program on the sample CSV, but it is NOT evidence of an actual attack or production incident.
- Task 8 instructions are read-only checks and documentation prompts. Capture screenshots from your own Windows test machine. Do not claim a setting is present unless the screenshot shows it.
- Do not change production settings. Use an authorized lab/VM and keep a way to recover console access.

TASK 13 — RUN THE PYTHON DEFENSIVE TOOL
1. Extract this folder to a convenient path, e.g. Desktop\Windows_Practical_Evidence_Kit.
2. Open the extracted folder in File Explorer.
3. Click the address bar, type cmd, and press Enter.
4. Run:
   py --version
   py authlog_sentinel.py sample_auth.csv --threshold 3
5. Expected output:
   Events processed: 6
   Failed-login combinations: 2
   ALERT: repeated failed logins
     username=admin source_ip=198.51.100.23 failures=3
   Review alerts with system, time-window, and user context.
6. Take a screenshot showing the command and complete output. Use Win+Shift+S or Snipping Tool.
7. Optional negative test:
   py authlog_sentinel.py sample_auth.csv --threshold 4
   Expected: no combinations meet the alert threshold.
8. Optional invalid-threshold test:
   py authlog_sentinel.py sample_auth.csv --threshold 0
   Expected: command-line validation error saying threshold must be at least 1.

TASK 8 — WINDOWS CONFIGURATION REVIEW (READ-ONLY EVIDENCE)
A. Windows version:
   Press Win+R, enter winver, press Enter.
   Screenshot: Windows version dialog. Caption it "Host identification (lab machine)".

B. Remote Desktop and NLA:
   Press Win+R, enter SystemPropertiesRemote, press Enter.
   Screenshot: Remote Desktop section showing current state and NLA checkbox if available.
   Do not enable/disable RDP solely for the screenshot. Caption the screenshot with the observed state.
   Note: menu/wording may vary by Windows edition/version. If the dialog is unavailable, record "Not available on this edition" rather than inventing a result.

C. Windows Firewall:
   Open Start and search "Windows Defender Firewall with Advanced Security".
   Open it and screenshot the Overview page showing profiles and current state.
   For rule evidence, open Inbound Rules and capture a selected rule's name, enabled status, action, protocol/ports, and scope. Avoid exposing sensitive hostnames/IPs in the report.
   Do not disable firewall or create broad allow rules.

D. Windows Update:
   Open Settings > Windows Update (Windows 10/11) and screenshot update status and last check/install details if shown.
   On older Windows versions, use Control Panel > Windows Update.
   Redact account names or other private information if visible.

E. Local Administrators group (read-only):
   Open Command Prompt and run:
   net localgroup Administrators
   Screenshot the command and output. Do not publish usernames publicly; redact them in the PDF if needed.
   If your system is domain-managed, some groups may be centrally controlled. Do not change membership.

F. Security/audit logs (read-only):
   Open Event Viewer > Windows Logs > Security.
   If access is allowed, filter or inspect recent event records and capture only a redacted example. Do not assert failed-logon auditing is enabled unless matching events/settings are visible.
   You may also record "Not accessible on this account" if permission is denied.

SCREENSHOT CHECKLIST
[ ] T8-01 winver host/version screenshot
[ ] T8-02 Remote Desktop/NLA current-state screenshot
[ ] T8-03 Windows Firewall Overview screenshot
[ ] T8-04 One relevant inbound firewall rule details screenshot
[ ] T8-05 Windows Update status screenshot
[ ] T8-06 net localgroup Administrators output (redact usernames)
[ ] T8-07 Event Viewer Security log example (redact identifiers; if accessible)
[ ] T13-01 Python version + successful tool run and output
[ ] T13-02 threshold=4 negative test
[ ] T13-03 threshold=0 validation test

REPORT CAPTION TEMPLATE
Evidence ID:
Task:
Date/time:
System: Windows (include edition/version if visible)
Action performed:
Observed result:
Interpretation:
Limitations:
Redactions applied:

EVIDENCE INTEGRITY
- Keep original screenshots unchanged in an Evidence folder.
- Do not paste fabricated outputs into a terminal screenshot.
- Use captions to distinguish actual machine screenshots from synthetic test data.
- If a check cannot be performed, state that clearly rather than claiming success.
