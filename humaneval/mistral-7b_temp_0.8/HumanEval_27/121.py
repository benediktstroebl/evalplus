

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    if isinstance(string, str):
        string = string.lower()
        string = string.upper()
        return string
    else:
        print("You must pass a string")

