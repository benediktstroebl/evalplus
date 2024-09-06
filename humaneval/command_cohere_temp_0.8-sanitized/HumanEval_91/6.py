def is_bored(S):
    """
    Count the number of boredoms in the given string.
    A boredom is a sentence that starts with the word "I".
    """
    boredoms = 0
    for line in S.split('.'):
        line = line.strip('!?')
        if line.startswith('I '):
            boredoms += 1
    return boredoms