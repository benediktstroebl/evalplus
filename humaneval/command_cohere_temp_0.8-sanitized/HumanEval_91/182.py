def is_bored(S):
    count = 0
    sentences = S.split('.')
    for sentence in sentences:
        sentence = sentence.strip('?,!')
        if sentence.startswith('I'):
            count += 1
    return count