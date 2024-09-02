
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    n_digits = len(str(abs(x))) # number of digits in abs x
    if shift > n_digits:
        return str(abs(x))[::-1]
    elif shift < -n_digits:
        return str(abs(x))[n_digits:n_digits+shift]
    else:
        return str(abs(x))[abs(shift):] + str(abs(x))[:abs(shift)]
        