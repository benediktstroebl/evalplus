
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
    words = S.split()
    count = 0
    for i in range(len(words)):
        if words[i] == "I":
            if i == 0:
                count += 1
            elif words[i - 1] != "." and words[i - 1] != "?" and words[i - 1] != "!":
                count += 1
    return count
