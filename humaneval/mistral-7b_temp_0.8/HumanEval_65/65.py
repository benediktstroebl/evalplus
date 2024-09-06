
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift > 0:
        if shift > len(x):
            return str(x)[::-1]
        return str(x)[shift:] + str(x)[:shift]
    if shift < 0:
        if shift < -len(x):
            return str(x)[::-1]
        return str(x)[len(x) + shift:] + str(x)[:len(x) + shift]
    return str(x)

