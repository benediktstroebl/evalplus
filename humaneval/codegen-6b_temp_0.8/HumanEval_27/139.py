

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i].isupper():
                string = string[:i]+string[i].lower()+string[i+1:]
    return string
