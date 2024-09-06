def is_bored(S):
    cnt = 0
    for sentence in S.split('. ') :
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('.') > -1:
            cnt += 1
    return cnt