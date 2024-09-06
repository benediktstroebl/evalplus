

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    flipped = ''
    for letter in string:
        if letter.isalpha():
            if letter.isupper():
                flipped += letter.lower()
            else:
                flipped += letter.upper()
        else:
            flipped += letter
    return flipped

