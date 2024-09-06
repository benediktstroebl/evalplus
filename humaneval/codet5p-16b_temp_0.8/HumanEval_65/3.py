
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    shift_digit = x % 10
    if shift_digit == 0:
        return str(x)
    else:
        remainder = x % (10 ** (shift - 1))
        result_x = x - remainder
    if shift_digit + shift > 10:
        return str(result_x)[::-1]
    else:
        return str(result_x + shift_digit * (10 ** (shift - 1)))[::-1]
