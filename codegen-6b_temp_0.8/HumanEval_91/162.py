
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
    
    # Split the sentence into tokens.
    tokens = S.split('.')
    # Count the number of "I" tokens.
    count = 0
    for token in tokens:
        if token.startswith("I "):
            count += 1
    return count


