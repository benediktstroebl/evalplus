

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Create a dictionary of characters and their flipped case
    char_map = {ord(char): ord(char.upper()) for char in string}
    # Iterate over the string using slicing
    return ''.join([char_map[char] if char in char_map else char for char in string])
