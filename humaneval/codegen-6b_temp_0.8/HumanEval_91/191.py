
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
    # use a list comprehension to count the number of 'I' from the string
    # after splitting the string by '.', '?' or '!', and then assign it to
    # a new variable.
    return sum(1 for sentence in S.split('.') 
               + S.split('?') 
               + S.split('!')
               if sentence.startswith('I'))

