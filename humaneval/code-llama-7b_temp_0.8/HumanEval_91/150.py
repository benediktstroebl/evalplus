
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
    count = 0
    # your code here
    # Hint: Start by initializing a counter at 0
    # Hint: Initialize the string to check at the first word
    # Hint: Using the modulo operator to check if there's a punctuation mark in the end of the string
    # Hint: Check if the string starts with "I"
    # Hint: If it does, add 1 to the counter
    # Hint: Check if the counter is greater than 0
    # Hint: If it is, return 1
    # Hint: If it is not, return 0
    # Hint: Split the string using the delimiters '.', '?' and '!'
    # Hint: Use a for loop and use the delimiters to delimit the strings
    # Hint: Use slicing to slice out the words
    # Hint: Use the .lower() method to lowercase the words
    return 0
