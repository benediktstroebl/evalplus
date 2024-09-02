
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
    # Your code here
    # You can use the following code snippet to convert the string to a list
    # and then sort the list based on its ascii value
    # Use a dictionary to store the string of characters in ascending order
    # and use it to replace the characters in the original string
    return ''.join(sorted(list(s)))
