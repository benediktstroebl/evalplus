

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    case_list = string.lower().split()
    return "".join([word.upper() if word.isupper() else word.lower() for word in case_list])

