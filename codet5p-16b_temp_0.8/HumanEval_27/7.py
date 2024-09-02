

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    lowercase = []
    uppercase = []
    for letter in string:
        if letter.isupper():
            lowercase.append(letter.lower())
            uppercase.append(letter.upper())
        else:
            lowercase.append(letter.upper())
            uppercase.append(letter.lower())
    return ''.join(lowercase) + ''.join(uppercase)
