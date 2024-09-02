

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flip_case_string = ""
    for char in string:
        if char.isupper():
            flip_case_string += char.lower()
        else:
            flip_case_string += char.upper()
    return flip_case_string

