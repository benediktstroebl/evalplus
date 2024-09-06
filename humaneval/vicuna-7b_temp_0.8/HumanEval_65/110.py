
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = list(str(x))
    while len(digits) > 0:
        n = len(digits) - 1
        digits[n], digits[0] = digits[0], digits[n]
        x = int(str(x)[:-1])
    return str(x)
