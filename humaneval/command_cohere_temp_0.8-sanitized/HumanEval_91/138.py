def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('?!')
        if sentence.startswith('I'):
            bored += 1
    return bored