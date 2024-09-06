
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
    # first option is a regular expression, but the problem is to avoid if
    # condition, so instead of that, i use a regular expression to extract the
    # words that starts with I.
    #
    # Using a regular expression:
    import re
    bored_sent = re.findall("I\w+", S)
    return len(bored_sent)

    # Solution 2:
    # S.count("I")
