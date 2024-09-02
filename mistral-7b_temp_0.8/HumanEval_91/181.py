
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
    n_bor = 0
    while S:
        if S.startswith("I"):
            n_bor += 1
            S = S[2:].strip()
            if not S:
                break
        if S[-1] in [".", "?", "!"]:
            S = S[:-1]
        elif S[-1] in ".,?!":
            S = S[:-1]
    return n_bor

