
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
    boredom_count = 0
    is_bored_bool = False
    for i in S.split("."):
        if "i" in i.lower():
            is_bored_bool = True
        else:
            is_bored_bool = False
        if is_bored_bool:
            boredom_count += 1
    return boredom_count

