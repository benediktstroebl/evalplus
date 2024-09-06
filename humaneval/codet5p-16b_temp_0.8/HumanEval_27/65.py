

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    upper_flag = False
    lower_flag = False
    final = ""
    for char in string:
        if char.isupper() and not upper_flag:
            final += char.lower()
            upper_flag = True
        elif char.islower() and not lower_flag:
            final += char.upper()
            lower_flag = True
        else:
            final += char
    return final
