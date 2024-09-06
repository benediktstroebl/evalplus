

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Use a dictionary to map lowercase characters to uppercase and uppercase characters to lowercase
    mapping = {ord(char): ord(char.upper()) for char in string}
    return ''.join(map(lambda x: mapping[x], string))