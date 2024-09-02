
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
    # A1.1.5
    #print(S)
    count = 0
    count_sentence = 0
    for s in S.split("."):
        count_sentence += 1
        #print(s)
        if s.strip() != "":
            if count_sentence > 1:
                if s.strip().startswith("I"):
                    count += 1
            else:
                if s.strip().startswith("I"):
                    count += 1
    return count



