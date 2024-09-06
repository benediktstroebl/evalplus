
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
    # use a dictionary to map each character to its ascii value
    # and then reverse the order of the characters
    char_map = {ord(c): c for c in s}
    reverse_map = {v: k for k, v in char_map.items()}
    result = ''
    for c in s:
        result += char_map[c]
    return result
