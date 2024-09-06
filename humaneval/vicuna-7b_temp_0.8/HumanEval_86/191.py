
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
    # assume the string is a concatenation of words separated by spaces
    words = s.split()
    # sort the words by their ASCII values
    words = sorted(words, key=lambda x: ord(x))
    # join the sorted words together to form the ordered string
    return ' '.join(words)
