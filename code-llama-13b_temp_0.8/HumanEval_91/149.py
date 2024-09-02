
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
    b = 0
    if not S:
        return b
    else:
        for i in S:
            if i.isalpha():
                b += 1
            elif i in ['.', '?', '!']:
                b = 0
            else:
                pass
            if i == 'I':
                b += 1
    return b
