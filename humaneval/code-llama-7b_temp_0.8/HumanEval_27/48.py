

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    if not isinstance(string, str):
        return string

    def flip(char):
        if char.islower():
            return char.upper()
        return char.lower()

    return ''.join(flip(char) for char in string)

