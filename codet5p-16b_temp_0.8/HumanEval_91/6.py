
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

    s=S.split('.')
    s1=[]
    for i in s:
        s1.extend(i.split('?'))
    s1.extend(s[0].split('!'))
    
    s2=[]
    for i in s1:
        if i.startswith('I'):
            s2.append(i)
    return len(s2)
