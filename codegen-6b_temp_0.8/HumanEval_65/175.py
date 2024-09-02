
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x = abs(x)
    # Make sure that shift is less than or equal to the number of digits
    shift = shift % len(str(x))
    if shift == 0:
        return str(x)
    n = len(str(x))
    digits = str(x)
    # List of digits in reverse order
    rev = [d for d in digits][::-1]
    return ''.join(rev[shift:n]) + ''.join(rev[0:shift])

