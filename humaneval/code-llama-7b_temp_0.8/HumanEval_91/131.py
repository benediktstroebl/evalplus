
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
    import re
    #your code here
    # return sum([s.startswith('I') for s in re.split(r'[\.\?\!]', S)])
    # I'd probably do something like
    # sentences = re.split(r'[\.\?\!]', S)
    # return sum(s.startswith('I') for s in sentences)
    # I'd probably do something like
    return sum(re.sub(r'[^\w]', ' ', s).count('i') for s in re.split(r'[\.\?\!]', S))
