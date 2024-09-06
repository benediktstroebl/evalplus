def is_bored(S):
    """
    Count the number of boredoms in the given string.
    A boredom is a sentence that starts with the word "I".
    Sentences are assumed to be delimited by '.', '?', or '!'.
    """
    boredoms = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?)').strip('i')
        if sentence.startswith('i'):
            boredoms += 1
    return boredoms