
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
    # s.split(' ') is a list of words separated by space in original string s.
    # Sorting by word, and then by character within each word, and then
    # joining the list back together will result in an 'ordered' string.
    return ' '.join(sorted(s.split(' '), key=lambda x: x.upper()))
