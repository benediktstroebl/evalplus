

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    string = string.upper() + string[1:]  # get the first letter as uppercase
    string = ''.join([ chr(ord('A') - i) if i < ord('A') else chr(ord(i) ^ 1) for i in string ])  # the rest of the characters in reverse order, with lowercase characters flipped to uppercase
    return string.lower()