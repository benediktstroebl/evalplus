
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
    s = 0
    for i in range(0,len(S)):
        if S[i]=='.' or S[i]=='?' or S[i]=='!':
            if S[s:i][0:2]=='I ':
                return 1
            else:
                s=i+1
        elif S[i]=='I':
            if S[i+1]==' ':
                return 1
    return 0

