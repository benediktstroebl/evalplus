
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    n = len(str(x))
    if shift > n:
        return ("1" * n + str(x)[0])[-shift:] + ("1" * n + str(x)[0])[:-shift]
    elif shift < n:
        return str(x)[-shift:] + str(x)[:-shift]
    else:
        return str(x)

