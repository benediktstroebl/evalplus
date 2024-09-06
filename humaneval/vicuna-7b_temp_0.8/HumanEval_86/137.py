
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
    char_map = {
        'a': '97', 'b': '98', 'c': '99', 'd': '100', 'e': '101', 'f': '102',
        'g': '103', 'h': '104', 'i': '105', 'j': '106', 'k': '107', 'l': '108',
        'm': '109', 'n': '110', 'o': '111', 'p': '112', 'q': '113', 'r': '114',
        's': '115', 't': '116', 'u': '117', 'v': '118', 'w': '119', 'x': '120',
        'y': '121', 'z': '122', '0': '48', '1': '49', '2': '50', '3': '51',
        '4': '52', '5': '53', '6': '54', '7': '55', '8': '56', '9': '57'
    }

    return ''.join(sorted(c[1] for c in s.split())).translate(str.maketrans('', '', char_map))