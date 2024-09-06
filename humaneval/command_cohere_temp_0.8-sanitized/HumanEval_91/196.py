def is_bored(S):
    """
    Count the number of boredoms in the given string.
    A boredom is a sentence that starts with the word "I".
    """
    boredoms = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?').strip()
        if sentence and sentence.startswith('I'):
            boredoms += 1
    return boredoms