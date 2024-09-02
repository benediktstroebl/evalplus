

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    flipped_string = ''

    for i in range(len(string)):
        if string[i].isupper():
            flipped_string += string[i].lower()
        elif string[i].islower():
            flipped_string += string[i].upper()
        else:
            flipped_string += string[i]

    return flipped_string

