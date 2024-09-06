def is_bored(S):
    cnt = 0
    for line in S.split('.') + S.split('?') + S.split('!'):
        if line.strip().lower().startswith('i'):
            cnt += 1
    return cnt