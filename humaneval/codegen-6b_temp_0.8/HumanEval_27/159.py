

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    upper_to_lower = {string[i].lower(): string[i].upper() for i in range(len(string))}
    return ''.join(upper_to_lower.get(letter, letter) for letter in string)
