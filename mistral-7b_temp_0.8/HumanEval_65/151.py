
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    l = len(str(x))
    if shift > l:
        return str(x)[::-1]
    if shift < 0:
        return str(x)[::-1][shift:] + str(x)[0:shift]
    return str(x)[shift:] + str(x)[0:shift]

