

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(sorted(string.lower()))

def reverse_string(string: str) -> str:
    """ For a given string, reverse the characters.
    >>> reverse_string('abc')
    'cba'
    """
    return ''.join(string[::-1])

def truncate(string: str, length: int) -> str:
    """ Truncate a string to a given length by either (a) removing the first n characters if the string is shorter,
    or (b) replacing any characters after the nth character with a specified filler character (e.g. '...').
    If the string is already exactly n characters long, it is returned as is.
    """
    if len(string) <= length:
        return string
    elif string.startswith('...'):
        # remove initial '...'
        return string[3:]
    else:
        # remove first n characters
        return string[:length]