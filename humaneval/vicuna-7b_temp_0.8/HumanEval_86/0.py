
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
    # convert string to lowercase
    s = s.lower()
    # split the string on white spaces
    words = s.split()
    # create a new string with the characters in ascending order
    new_string = ''
    for c in 'abcdefghijklmnopqrstuvwxyz':
        new_string += chr(ord(c) + 1)
    # join the words with the new string
    new_string += ''.join(words)
    return new_string
