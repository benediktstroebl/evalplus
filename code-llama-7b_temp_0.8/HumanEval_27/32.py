

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flip_case = ''
    for char in string:
        if char.isupper():
            flip_case += char.lower()
        else:
            flip_case += char.upper()
    return flip_case

