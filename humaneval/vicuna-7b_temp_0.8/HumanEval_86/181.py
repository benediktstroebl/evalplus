
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
    # Check if the input string is not empty
    if not s:
        return s

    # Split the input string into a list of words
    words = s.split()

    # Join the words in a new string with its characters in ascending order
    return ''.join([chr(ord('a') + i) for i in range(len(words))])
