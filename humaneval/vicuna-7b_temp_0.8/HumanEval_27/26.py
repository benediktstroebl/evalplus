

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(re.sub(r'[a-z]', r'\U'.join([chr(ord('A') + i) for i in range(12)]), string))
