

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper_to_lower = {upper[i]: lower[i] for i in range(len(upper))}
    lower_to_upper = {lower[i]: upper[i] for i in range(len(lower))}
    return string.translate(upper_to_lower).translate(lower_to_upper)

