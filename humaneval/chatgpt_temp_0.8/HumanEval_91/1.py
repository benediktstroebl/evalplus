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
    sentences = S.split(".")
    sentences = [s.strip() for s in sentences]
    sentences = [s for s in sentences if s]
    sentences = [s.split("?") for s in sentences]
    sentences = [s for sublist in sentences for s in sublist]
    sentences = [s.split("!") for s in sentences]
    sentences = [s for sublist in sentences for s in sublist]
    sentences = [s.strip() for s in sentences]
    boredoms = sum([1 for s in sentences if s.startswith("I")])
    return boredoms
