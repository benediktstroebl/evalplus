def is_bored(S):
    cnt = 0
    for line in S.splitlines():
        line = line.strip()  # Remove trailing spaces and tabs
        if line.startswith("I ") or line.startswith("i "):
            cnt += 1
    return cnt