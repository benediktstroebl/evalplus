
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
    # your code here
    # count = 0
    # for word in S.split():
    #     if word == "I":
    #         count += 1
    # return count

    # count = 0
    # for sentence in S.split(".") + S.split("!") + S.split("?"):
    #     if sentence.startswith("I"):
    #         count += 1
    # return count

    # count = 0
    # for sentence in S.split(".") + S.split("!") + S.split("?"):
    #     if sentence.split()[0] == "I":
    #         count += 1
    # return count

    # sentences = S.split(".") + S.split("!") + S.split("?")
    # count = sum([1 for sentence in sentences if sentence.split()[0] == "I"])
    # return count

    return sum([1 for sentence in S.split(".") + S.split("!") + S.split("?") if sentence.split()[0] == "I"])

