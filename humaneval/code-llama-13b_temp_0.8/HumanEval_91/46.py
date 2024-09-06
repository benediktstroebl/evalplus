
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
    s = S.strip()
    if len(s) == 0:
        return 0
    sent, bored = [], []
    for word in s.split():
        if word == "I":
            bored.append(word)
        if word == "." or word == "?" or word == "!":
            sent.append(" ".join(bored))
            bored = []
    return len(sent)

