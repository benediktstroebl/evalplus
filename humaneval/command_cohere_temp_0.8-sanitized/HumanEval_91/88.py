def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('.') + S.split('?') + S.split('!') if sentence.startswith('I'))
    return boredom_count