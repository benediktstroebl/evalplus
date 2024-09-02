

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    
    new_string = ""
    for i in string:
        if i.isupper():
            new_string += i.lower()
        elif i.islower():
            new_string += i.upper()
    return new_string
