

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped = []
    for letter in string:
        if letter.isupper():
            flipped.append(letter.lower())
        else:
            flipped.append(letter.upper())
    return ''.join(flipped)
