
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
    count = 0
    if len(S.split()) == 1:
        if S.startswith("I"):
            count += 1
        return count
    for i in S.split(".") + S.split("?") + S.split("!"):
        if i.startswith("I"):
            count += 1
    return count
