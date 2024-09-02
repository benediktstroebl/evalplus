

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # sort the string by converting it to lowercase and uppercase
    string = string.lower() + string.upper()
    # use a dictionary to map each character to its flipped version
    flip_map = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F',
                'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L',
                'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R',
                's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X',
                'y': 'Y', 'z': 'Z'}
    # iterate through the sorted string and flip each character
    result = ''
    for char in string:
        result += flip_map[char]
    return result