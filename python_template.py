"""
RECORD CHECK  -  my version
===========================

Name  : Yousef Alsuwaidi
Lane  :  Cyber Security
Date  : 12/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Defines a new parse log."""

    line = raw_line.strip()

    source_part, rest = line.split(",", 1)

    result = {"src": source_part.strip().lower()}

    for piece in rest.split(","):
        key, value = piece.split("=")
        result[key.strip().lower()] = value.strip().lower()

    return result


def status_of(record):
    """Return FLAGGED if login failed or register it as OK."""

    if record["result"] == "failed":
        return "FLAGGED"
    return "OK"


# ====================================================================== INPUT

raw_records = [
    "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED",
    " src=192.168.1.10 , attempts=3 , result=success ",
    "SRC=172.16.0.8,ATTEMPTS=7,RESULT=FAILED",
    " Src=10.1.1.20 , Attempts=1 , Result=Success ",
    "SRC=192.168.100.12,ATTEMPTS=15,RESULT=FAILED"
]


# =============================================================== PROCESS + OUTPUT

flagged_count = 0

for raw_record in raw_records:
    record = parse_line(raw_record)

    print(record)

    status = status_of(record)
    print("Status:", status)

    if status == "FLAGGED":
        flagged_count += 1

print()
print("Summary")
print("Records processed:", len(raw_records))
print("Flagged records:", flagged_count)


# ==========================================================================