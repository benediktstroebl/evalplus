

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    lc_chars = list(string)

    for i, ch in enumerate(lc_chars):
        if ch.islower():
            lc_chars[i] = ch.upper()
        elif ch.isupper():
            lc_chars[i] = ch.lower()

    return ''.join(lc_chars)

