

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    return ''.join(
        'h' if letter.islower() else 'H' if letter.isupper() else letter
        for letter in string
    )
