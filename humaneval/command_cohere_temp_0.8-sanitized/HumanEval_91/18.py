def is_bored(S):
    cnt = 0
    for line in S.splitlines():
        line = line.strip() 
        if line.startswith("I ") and (line.endswith(".") or line.endswith("?") or line.endswith("!")): 
            cnt += 1
    return cnt