
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
    # Your code here
    res = 0
    str = S.split()
    if len(str) > 2:
        for i in range(0, len(str)-2):
            if str[i] == "I" and (str[i+1] == "." or str[i+1] == "?" or str[i+1] == "!"):
                res += 1
    return res
