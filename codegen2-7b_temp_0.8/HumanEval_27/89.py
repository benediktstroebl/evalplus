

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_string = ''
    for letter in string:
        if letter.isupper():
            new_string += letter.lower()
        elif letter.islower():
            new_string += letter.upper()
    return new_
