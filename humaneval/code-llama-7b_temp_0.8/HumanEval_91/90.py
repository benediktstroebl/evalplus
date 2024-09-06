
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
    bored_count = 0
    bored = False
    for x in S.split("."):
        if x.startswith("I"):
            bored = True
        elif x.strip()[-1] in ".!?" and bored:
            bored_count += 1
            bored = False
    return bored_count
