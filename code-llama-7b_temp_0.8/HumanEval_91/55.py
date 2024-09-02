
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """

    # This problem can be solved recursively or iteratively.
    # Solution is recursive
    # Split on any of '!', '.' or '?', and count boredom if first word is 'I'.
    # Separated by either '!', '.' or '?'
    if len(S) < 3:
        return 0
    else:
        S = S.split('!')
        for sentence in S:
            sentence = sentence.split('.')
            for phrase in sentence:
                phrase = phrase.split('?')
                for phrase in phrase:
                    phrase = phrase.split()
                    try:
                        if phrase[0] == 'I':
                            return 1
                    except:
                        pass
    return 0
