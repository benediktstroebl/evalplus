
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
    # your code here
    
    i = 0
    count = 0
    flag = 0
    for s in S:
        if s.isalpha():
            if s.islower():
                i += 1
            else:
                i = 0
        elif s.isspace():
            i = 0
        else:
            i = 0
        if i == 2:
            if s == '.':
                i = 0
                flag = 1
            elif s == '!' or s == '?':
                i = 0
                flag = 1
            else:
                i = 0
        elif i == 1:
            if flag == 1:
                count += 1
                flag = 0
    return count
