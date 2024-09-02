

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # your code here
    result = ''
    for ch in string:
        if ch.isupper():
            result += ch.lower()
        elif ch.islower():
            result += ch.upper()
        else:
            result += ch
    return result
