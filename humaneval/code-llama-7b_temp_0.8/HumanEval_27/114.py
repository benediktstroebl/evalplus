

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    if not string:
        return string

    output = ""
    for letter in string:
        output += letter.swapcase()

    return output

