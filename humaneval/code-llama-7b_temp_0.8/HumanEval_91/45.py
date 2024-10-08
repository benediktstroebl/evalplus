
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

    # todo: [WORK IN PROGRESS]
    result = 0
    words = S.split(" ")
    for i in range(0, len(words)):
        if words[i] == "I":
            result += 1
        if (words[i + 1] == "." or words[i + 1] == "?" or words[i + 1] == "!") and words[i] != "I":
            result += 1
    return result
