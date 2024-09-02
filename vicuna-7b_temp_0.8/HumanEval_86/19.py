
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    # Solution goes here
    # The function takes a string as input and returns an ordered version of it
    # The ordered version of the string is a new string where all the characters
    # in the original string are arranged in ascending order based on their ASCII value
    # The function should keep the order of words and blank spaces in the original string

    # Example: 'Hi' -> 'H i'
    # Example: 'hello' -> 'e hllo'
    # Example: 'Hello World!!!