
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
    I = 0
    for i in range(len(S)):
        if i == len(S)-1:
            return I
        if S[i] == "I" and (S[i+1] == "." or S[i+1] == "?" or S[i+1] == "!"):
            I = I + 1
    return I

    #you can do a for loop to go through each element of the string
    #you can increment a counter to keep track of how many times it says "i"
    #you can use string slicing to find the next punctuation mark
    #you can use the .index method to find the location of the next punctuation mark
    #you can use a boolean expression to make sure the next punctuation mark is not a "!"
    #you can use a boolean expression to make sure the next punctuation mark is not a "?"
    #you can use a boolean expression to make sure the next punctuation mark is not a "."
    #you can use a boolean expression to make sure the next punctuation mark is not a "i"
    #you can use a
