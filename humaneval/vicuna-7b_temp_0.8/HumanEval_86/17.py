
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
    # Use a list to store the characters of the string
    char_list = [ord(c) for c in s]

    # Sort the characters in ascending order
    char_list.sort()

    # Create a new string with the sorted characters in the same order
    new_string = ''.join([chr(i) for i in char_list])

    return new_string
