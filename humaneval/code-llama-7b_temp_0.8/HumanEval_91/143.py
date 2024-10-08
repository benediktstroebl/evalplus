
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
    a = S.split('.')
    b = S.split('?')
    c = S.split('!')
    d = a+b+c
    if any(sentence.strip().startswith("I") for sentence in d):
        return 1
    return 0


