

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped = []
    for letter in string:
        if letter.isupper():
            flipped.append(letter.lower())
        elif letter.islower():
            flipped.append(letter.upper())
        else:
            flipped.append(letter)

    return ''.join(flipped)
