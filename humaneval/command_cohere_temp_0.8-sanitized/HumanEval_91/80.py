def is_bored(S):
    count = 0
    sentences = S.split('。')
    for sentence in sentences:
        if sentence.strip()[0] == 'I':
            count += 1
    return count