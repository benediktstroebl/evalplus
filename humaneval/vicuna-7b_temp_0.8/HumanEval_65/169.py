
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = [str(d) for d in x]
    shift_left = [d + '0'*(len(str(d)) - len(str(next(digits)))) for d in digits]
    shift_right = [next(digits) + '0'*(len(str(next(digits))) - len(str(d))) for d in digits]
    return ''.join(shift_left[::-1]) + ''.join(shift_right)
