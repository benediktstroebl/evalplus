
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

    s = S.split(".")
    s1 = s[0].split("?")
    s2 = s[0].split("!")
    
    boredom = len(s1) + len(s2)
    
    for i in range(1, len(s)):
        s3 = s[i].split("?")
        s4 = s[i].split("!")
        boredom += len(s3) + len(s4)
    return boredom

