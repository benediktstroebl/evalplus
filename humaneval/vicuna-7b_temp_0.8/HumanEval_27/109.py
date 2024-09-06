

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Convert all characters to lowercase
    string = string.lower()
    # Convert all characters to uppercase
    string = string.upper()
    # Reverse the string
    string = string[::-1]
    # Convert the reversed string back to lowercase
    string = string.lower()
    return string