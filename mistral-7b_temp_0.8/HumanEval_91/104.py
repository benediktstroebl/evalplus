
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
    # TODO: replace this line with your code
    n = 0
    count = 0
    for i in range(0, len(S)):
        if S[i] == "." or S[i] == "!" or S[i] == "?":
            count = 0
            n += 1
        elif S[i] == "I":
            count += 1
            if count == 1:
                n += 1
    return n
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_bored("Hello world") == 0, "1st example"
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1, "2nd example"
    assert is_bored("") == 0, "3rd example"
    assert is_bored("I") == 1, "4th example"
    assert is_bored("I...I...I") == 2, "5th example"
    assert is_bored("I love you.
