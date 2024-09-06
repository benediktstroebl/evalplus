

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Define a regular expression to match lowercase characters
    re_lower = re.compile(r'[a-z]', re.IGNORECASE)
    # Define a regular expression to match uppercase characters
    re_upper = re.compile(r'[A-Z]')
    # Convert the input string to a list of characters
    chars = string.split()
    # Create a dictionary to map characters to their flipped version
    char_map = {re_lower.sub(chr(ord(c) ^ 32), c) for c in chars}
    # Convert the dictionary of characters to a string
    return ''.join(char_map)
