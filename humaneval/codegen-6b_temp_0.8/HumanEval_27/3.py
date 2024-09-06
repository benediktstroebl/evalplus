

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    
    flipped_string = ''
    for ltr in string:
        if (ltr.islower()):
            flipped_string += ltr.upper()
        else:
            flipped_string += ltr.lower()
    return flipped_string
