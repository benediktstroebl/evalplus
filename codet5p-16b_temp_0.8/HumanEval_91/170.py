
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
    s = S.split('.')
    s = [i.split(' ') for i in s]
    s = [i for i in s if len(i)>0]
    s = [[i.strip() for i in j if len(i)>0] for j in s]
    s = [[i for i in j if i.startswith('I')] for j in s]
    s = [i for i in s if len(i)>0]
    return len(s)
    
