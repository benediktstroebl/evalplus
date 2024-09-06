
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if len(str(x)) == 1:
        return str(x)
    result = str(x)[0]
    for i in range(shift):
        result = str(x)[1] + result
    if len(str(x)) > 1:
        result = str(x)[:-1] + result
    return result
