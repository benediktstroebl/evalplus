

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flip = list(string)

    for i in range(len(flip)):
        if flip[i].isupper():
            flip[i] = flip[i].lower()
        else:
            flip[i] = flip[i].upper()
    return "".join(flip)
