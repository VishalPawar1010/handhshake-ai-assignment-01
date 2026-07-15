import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def _load_report():
    assert REPORT_PATH.exists(), f"{REPORT_PATH} not found"
    with open(REPORT_PATH) as f:
        return json.load(f)


def test_total_requests():
    """Criterion 2: total_requests matches the true number of request lines."""
    report = _load_report()
    assert report.get("total_requests") == 6, (
        f"expected total_requests == 6, got {report.get('total_requests')!r}"
    )


def test_unique_ips():
    """Criterion 3: unique_ips matches the true number of distinct client IPs."""
    report = _load_report()
    assert report.get("unique_ips") == 3, (
        f"expected unique_ips == 3, got {report.get('unique_ips')!r}"
    )


def test_top_path():
    """Criterion 4: top_path matches the most-requested path in the log."""
    report = _load_report()
    assert report.get("top_path") == "/index.html", (
        f"expected top_path == '/index.html', got {report.get('top_path')!r}"
    )