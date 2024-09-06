

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    s = string.upper()
    for i in range(len(s)):
        if s[i].islower():
            s = s.replace(s[i], s[i].upper())
    return s
