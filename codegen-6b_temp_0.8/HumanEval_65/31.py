
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    max = len(str(x))
    shifted = str(int(str(x)[max - shift:] + str(x)[:max - shift]))
    return shifted if shift > max else shifted[::-1]
