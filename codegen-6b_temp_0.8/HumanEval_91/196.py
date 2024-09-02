
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
    # start index of 'I'
    # end index of 'I'
    # start index of 'I'
    # end index of 'I'
    # count
    # s=0
    # e=0
    # i=0
    # for char in S:
    #     if char =='.':
    #         s=i
    #         e+=1
    #     elif char =='?':
    #         s=i
    #         e+=1
    #     elif char =='!':
    #         s=i
    #         e+=1
    #     i+=1
    # return s-e
    return sum(1 for char in S if char in ('!','?','.'))
