
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
    sentence_delimiters = (".", "?", "!")
    S = S.replace("?", ".").replace("!", ".")
    result = 0
    for word in S.split():
        if word == "I" and S[S.index(word) - 1] in sentence_delimiters:
            result += 1
    return result
