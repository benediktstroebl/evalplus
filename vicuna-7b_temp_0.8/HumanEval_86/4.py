
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
    # Use a list of strings to store the words of the input string
    words = s.split()

    # Sort the list of words based on their ASCII value
    words.sort(key=lambda x: x.isalpha())

    # Join the words together in the order they appear in the input string
    return ' '.join(words)
