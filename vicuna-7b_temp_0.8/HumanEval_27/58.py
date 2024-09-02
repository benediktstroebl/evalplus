

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # convert the string to lowercase and flip the characters
    string = string.lower().encode('utf-8')
    flipped = [chr(ord(c) ^ 32) for c in string]
    return ''.join(flipped)
