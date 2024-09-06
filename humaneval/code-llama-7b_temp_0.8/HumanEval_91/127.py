
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
    # Your code here
    S=S.split()
    index=0
    count=0
    while index<len(S):
        if S[index]=="I":
            count+=1
            if S[index+1]==".":
                index+=2
                continue
            elif S[index+1]=="!":
                index+=2
                continue
            else:
                index+=1
                continue
        else:
            index+=1
    return count
