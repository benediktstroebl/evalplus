def is_bored(S):
    cnt = 0
    for sentence in S.split('. ') + S.split('? ') + S.split('! '):
        if sentence.startswith('I'):
            cnt += 1
    return cnt