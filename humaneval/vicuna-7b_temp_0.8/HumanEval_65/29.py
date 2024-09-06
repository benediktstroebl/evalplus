
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    result = ""
    for i in range(1, min(len(str(x)), shift+1)):
        result = str(x)[i-1] + result
    if shift > len(str(x)):
        result = str(x)[::-1]
    return result
