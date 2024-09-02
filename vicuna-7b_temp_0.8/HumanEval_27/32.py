

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([ord(char) - ord('A') + 25 if ord(char) >= ord('A') else ord(char) - ord('a') + 25 for char in string])
