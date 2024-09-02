
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
    S = S.split('.')
    S2 = [s.strip() for s in S]
    return sum(len(s) for s in S2 if s.lower().startswith('i'))

try:
    import doctest
    doctest.testmod()
except ImportError:
    pass
