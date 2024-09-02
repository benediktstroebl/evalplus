

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = list(string)
    for index, value in enumerate(string):
        if value.isupper():
            string[index] = value.lower()

        if value.islower():
            string[index] = value.upper()
    return ''.join(string)
