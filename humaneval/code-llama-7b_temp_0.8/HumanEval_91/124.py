
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
    is_bored = 0
    # print(S)
    words = S.split(" ")
    # print(words)

    for i in range(len(words)):
        # print(words[i])
        if words[i] == "I":
            for j in range(i + 1, len(words)):
                # print(words[j])
                if words[j] == ".":
                    return is_bored + 1
                elif words[j] == "!":
                    return is_bored + 1
                elif words[j] == "?":
                    return is_bored + 1
                else:
                    pass
        else:
            pass
    return is_bored

