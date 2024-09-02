
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

    if s == '':
        return ''

    # If string does not contain a space, it is already in sorted order
    if ' ' not in s:
        return s

    # Create a list of words in s
    words = s.split()

    # Sort each word
    words = [sorted(word) for word in words]

    # Return a string with space separated words
    return ' '.join(words)
