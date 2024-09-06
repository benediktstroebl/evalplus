

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    
    lower_case_set = 'abcdefghijklmnopqrstuvwxyz'
    upper_case_set = lower_case_set.upper()
    
    return string.lower() if string.isupper() else string.upper
