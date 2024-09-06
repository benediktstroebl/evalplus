
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
    S = S.lower() # make sure the string is all lowercase
    words = S.split(".?!") # split the string into words
    boredoms = 0 # count the boredoms
    for word in words:
        if word.startswith("i"):
            boredoms += 1 # if the word starts with "I", it's a boredom
    return boredoms
