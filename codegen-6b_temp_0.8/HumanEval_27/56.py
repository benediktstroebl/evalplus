

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    for letter in string:
        if letter.isupper():
            yield letter.lower()
        elif letter.islower():
            yield letter.upper()
        else:
            yield letter

