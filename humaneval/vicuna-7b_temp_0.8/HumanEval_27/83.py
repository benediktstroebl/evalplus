

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # use a dictionary to map lowercase characters to their uppercase equivalents
    # and uppercase characters to their lowercase equivalents
    # initialize the dictionary
    d = {e.upper(): e for e in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if e.upper() != e}
    # iterate through the characters in the string
    for char in string:
        # if the character is in the dictionary
        if char.upper() in d:
            # flip the character
            string = string.replace(char, d[char.upper()])
        # if the character is not in the dictionary, don't change it
    return string
