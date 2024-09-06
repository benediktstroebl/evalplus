def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('. ') if sentence.strip()[0] == 'I')
    return boredom_count