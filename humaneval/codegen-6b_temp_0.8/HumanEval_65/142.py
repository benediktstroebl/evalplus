
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    num_digits = len(str(abs(x)))
    if shift > num_digits:
        return str(abs(x))[::-1]

    shifted_str = str(abs(x))[shift:] + str(abs(x))[:shift]
    return shifted_str

