
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
    count=0
    for i in range(0,len(S)):
        if S[i]=='.' or S[i]=='?' or S[i]=='!':
            count+=1
    list1=S.split('.')
    list1.pop()
    for i in range(0,len(list1)):
        if(list1[i].startswith('I')):
            count+=1
    return count
