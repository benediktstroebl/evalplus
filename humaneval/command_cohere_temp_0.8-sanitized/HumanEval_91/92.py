def is_bored(S):
    """
    Count the number of boredoms in the given string.
    A boredom is a sentence that starts with the word "I".
    """
    boredoms = sum(1 for sentence in S.split('. ') if sentence.startswith('I'))
    return boredoms