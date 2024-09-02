
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    try:
        s = str(x)
    except ValueError:
        return str(x)

    if len(s) == 0:
        return s

    if s[0] == "0":
        return s[1:]

    return s + s[0] + s[1:]
