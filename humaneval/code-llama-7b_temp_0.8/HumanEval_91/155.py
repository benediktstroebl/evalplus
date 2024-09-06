
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
    a = S.split(".")
    b = 0
    for i in range(0,len(a)):
        if(len(a[i].strip()) == 0):
            continue
        if(len(a[i].split(" ")) == 1):
            continue
        else:
            if(a[i].split(" ")[0].strip() == "I"):
                b = b+1
    return b

