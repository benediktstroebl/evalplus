
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
    #
    # set for the sentences
    sent_set = set()
    # if the first word is not I, we can skip
    if S[0] != "I":
        return 0
    # loop through the string and grab the first word
    for i in range(0, len(S), 3):
        # get the string from the index up to the first space
        sent = S[i:S.find(" ", i)]
        # if the first word is I, add it to the set
        if sent[0] == "I":
            sent_set.add(sent)
    return len(sent_set)
