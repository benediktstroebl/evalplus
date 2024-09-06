def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('. ') if sentence.lower().startswith('i'))
    return boredom_count