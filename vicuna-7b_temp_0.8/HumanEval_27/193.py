

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # convert the string to a list of characters
    characters = string.split()
    # iterate over the list and flip the characters
    for i, c in enumerate(characters):
        if c.islower():
            characters[i] = c.upper()
        elif c.isupper():
            characters[i] = c.lower()
    # join the characters back into a string
    return ''.join(characters)
