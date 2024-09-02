
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    """
    Idea: keep two indices, one for iterating through string,
    one for indexing into the shifted string (mod length)
    """
    digits = [d for d in str(x)]
    idx = shift
    string = ''

    while idx < len(digits):
        string += digits[idx]
        idx += 1

    if idx >= len(digits):
        string += ''.join(digits[:idx - len(digits)])

    return string

