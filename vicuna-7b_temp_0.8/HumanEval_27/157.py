

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Set up a dictionary with mapping of characters and their case
    char_map = {'a': 'A', 'b': 'B', ...}
    # Iterate over the string
    for char in string:
        # If the character is already in the correct case, just append it
        if char.upper() == char:
            yield char
        # Otherwise, flip the case of the character and append it
        else:
            yield char_map[char.upper()]