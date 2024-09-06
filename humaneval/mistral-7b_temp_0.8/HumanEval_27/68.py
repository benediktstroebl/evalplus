

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = list(string)
    for i, char in enumerate(string):
        if char.isupper():
            string[i] = char.lower()
        elif char.islower():
            string[i] = char.upper()
    return "".join(string)

