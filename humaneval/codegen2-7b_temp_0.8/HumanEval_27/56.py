

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    lower_case = string.lower()
    upper_case = string.upper()
    return lower_case if lower_case == upper_case else upper_case + lower_case[1:
