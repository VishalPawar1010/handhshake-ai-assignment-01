There's an Apache-style access log at /app/access.log in the working directory. Parse it and write a JSON summary report to /app/report.json.

The report must be a JSON object with exactly these three keys:

1. total_requests — the total number of request lines in the log file.
2. unique_ips — the number of distinct client IP addresses (the first field on each line) that appear in the log.
3. top_path — the single request path (e.g. "/index.html") that appears most often across all requests.

Format example (values below are illustrative only, not the answer):
{"total_requests": 42, "unique_ips": 7, "top_path": "/some/path"}

Success criteria:
1. /app/report.json exists and contains valid JSON.
2. total_requests exactly matches the true number of request lines in /app/access.log.
3. unique_ips exactly matches the true number of distinct client IPs in /app/access.log.
4. top_path exactly matches the most-requested path in /app/access.log.