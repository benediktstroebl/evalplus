

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = []
    for char in string:
        if char.isupper():
            char = char.lower()
        elif char.islower():
            char = char.upper()
        result.append(char)
    return "".join(result)

