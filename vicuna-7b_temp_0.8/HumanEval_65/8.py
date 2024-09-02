
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    sign = "-" if x < 0 else "+"
    x = int(x)
    n = len(str(x))
    if shift == 0:
        return sign + str(x)
    elif shift < n:
        return sign + str(x)[-shift-1:] + str(x)[-n+shift+1]
    else:
        return sign + str(x)[-n+shift+1:] + str(x)[-n+1]
