

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    new_str = list(string)
    for i in range(len(string)):
        if string[i].isupper():
            new_str[i] = string[i].lower()
        elif string[i].islower():
            new_str[i] = string[i].upper()
    return ''.join(new_str)
    
