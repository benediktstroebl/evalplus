
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
    i=0
    l=[]
    while i<len(S):
        if S[i]=="I":
            j=i+1
            while j<len(S):
                if S[j]=="." or S[j]=="?" or S[j]=="!":
                    l.append(i)
                    break
                else:
                    j=j+1
        i=i+1
    return len(l)
    # You can test your function by uncommenting the next two lines
    print(is_bored("Hello world"))
    print(is_bored("The sky is blue. The sun is shining. I love this weather"))

