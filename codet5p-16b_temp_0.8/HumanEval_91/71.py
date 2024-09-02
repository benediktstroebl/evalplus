
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

    boredom = 0
    for i in S.split():
        if i.startswith('I') and (i!= 'I am') and (i!= 'I want') and (i!= 'I would') and (i!= 'I do'):
            boredom += 1
    return boredom
