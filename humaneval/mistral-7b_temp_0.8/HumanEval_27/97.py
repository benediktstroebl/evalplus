

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = list(string)
    for char in string:
        if char.islower():
            string.remove(char)
            string.append(char.upper())
        elif char.isupper():
            string.remove(char)
            string.append(char.lower())
    return "".join(string)

