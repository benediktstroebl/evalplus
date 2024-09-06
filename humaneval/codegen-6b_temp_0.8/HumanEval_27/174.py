

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    '''
    res = []
    for letter in string:
        if letter.isupper():
            res.append(letter.lower())
        elif letter.islower():
            res.append(letter.upper())
        else:
            res.append(letter)
    return ''.join(res)
    '''

    return string.swapcase()

