

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    case_chars = list(string)
    for i in range(len(case_chars)):
        char = case_chars[i]
        if char in string.lower():
            case_chars[i] = char.upper()
        elif char in string.upper():
            case_chars[i] = char.lower()
    return "".join(case_chars)

