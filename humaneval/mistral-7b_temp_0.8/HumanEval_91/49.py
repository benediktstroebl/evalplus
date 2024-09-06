
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
    # TODO
    # count the number of words starting with "I"
    # in each sentence
    # a sentence is delimited by '.', '?' or '!'

    sentence_count = 0
    # for sentence in S.split():
    #     sentence_count += 1
    #     if sentence.startswith("I"):
    #         return sentence_count
    # return 0
    return S.count("I")
    #
    # is_bored("Hello world")
    # is_bored("The sky is blue. The sun is shining. I love this weather")

