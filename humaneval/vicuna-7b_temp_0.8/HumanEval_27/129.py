

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Let's convert the string to lowercase or uppercase
    # depending on the case of the first character
    # We use the Python built-in function lower() or upper()
    # and the string's length to store the string in a variable
    string_lower = ''.join([string[i:i+1] if i+1 < len(string) else string[i]) for i in range(len(string)-1)]
    string_upper = ''.join([string[i:i+1].upper() if i+1 < len(string) else string[i].upper() for i in range(len(string)-1)])
    
    return string_lower if string_lower.lower() != string_lower else string_upper
