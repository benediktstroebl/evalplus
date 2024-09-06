
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    y = x % 10
    result = x
    while shift > 0:
        if shift > 1:
            result = (result % 10) * 10 + (y % 10)
        else:
            result = (result % 10) * 10
        y = result % 10
        shift -= 1
    return str(result
