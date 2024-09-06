

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flip = ''
    for letter in string:
        if letter.isupper():
            flip += letter.lower()
        elif letter.islower():
            flip += letter.upper()
        else:
            flip += letter
    return flip

