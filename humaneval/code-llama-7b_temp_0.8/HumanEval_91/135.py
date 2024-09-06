
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
    assert len(S) > 0, "S must be non-empty"
    assert type(S) == str, "S must be a string"
    s = S.replace('.', ' .').replace('?', ' ?').replace('!', ' !')
    return len([s for s in s.split() if s == 'I'])
