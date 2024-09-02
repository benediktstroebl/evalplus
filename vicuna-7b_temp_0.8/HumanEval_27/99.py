

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join([ord(c) - ord('A') + 25 if c.islower() else ord(c) - ord('A') + 25 if c.isupper() else c for c in string])
