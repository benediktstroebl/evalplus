def is_bored(S):
    """
    Count the number of boredoms in the given string.
    A boredom is a sentence that starts with the word "I".
    Sentences are assumed to be delimited by '.', '?', or '!'.
    """
    bores = sum(1 for sentence in S.split('.') + S.split('?') + S.split('!') if sentence.startswith('I'))
    return bores