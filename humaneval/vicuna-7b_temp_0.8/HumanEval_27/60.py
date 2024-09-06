

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return "".join([chr(ord("A") - 32 + (x - 97 if x.isupper() else x.islower())) if x.isupper() else chr(ord(x) - 97) if x.islower() else x for x in string])
