

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ""
    for char in string:
        result += chr(ord(char) + 32) if ord(char) >= 65 and ord(char) <= 90 else chr(ord(char) - 32) if ord(char) >= 97 and ord(char) <= 122 else char
    return result

