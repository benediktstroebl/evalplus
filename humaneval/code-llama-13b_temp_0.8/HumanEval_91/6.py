
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
    boredom_cnt = 0
    boredom = False
    for i in range(len(S)):
        if boredom:
            if S[i] == ' ':
                continue
            elif S[i] == '.' or S[i] == '!' or S[i] == '?':
                boredom = False
                boredom_cnt += 1
            else:
                boredom = True
        else:
            if S[i] == 'I':
                boredom = True
    return boredom_cnt

