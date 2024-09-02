

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ''
    for letter in string:
        result += letter.upper() if letter.islower() else letter.lower()
    return result

