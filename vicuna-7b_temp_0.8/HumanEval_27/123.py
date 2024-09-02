

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # create a set of characters to be modified
    modified_chars = set(string.upper()) | set(string.lower())

    # initialize a new string to store the modified characters
    modified_string = ''

    # iterate over the original string
    for char in string:
        # if the character is in the modified characters set, flip it
        if char in modified_chars:
            modified_string += flip_case[char]
        else:
            modified_string += char

    return modified_string