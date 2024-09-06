
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if type(x) is not int:
        raise TypeError("argument x must be of type 'int'")
    if type(shift) is not int:
        raise TypeError("argument shift must be of type 'int'")
    result = str(x)
    if shift < 0:
        shift *= -1
        result = result[::-1]
    result = result[-shift:] + result[:-shift]
    if shift < len(str(x)):
        result = result[::-1]
    return result
