

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Your code here
    result = ""
    for c in string:
        if c.isupper():
            result += c.lower()
        else:
            result += c.upper()
    return result

