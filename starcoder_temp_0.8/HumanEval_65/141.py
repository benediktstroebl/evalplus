
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x_digits = []
    while x > 0:
        x_digits.append(x % 10)
        x //= 10
    shift_digits = len(x_digits)
    if shift > shift_digits:
        shift = shift - shift_digits
        return ''.join(str(x_digits[i]) for i in range(len(x_digits)))
    else:
        return ''.join(str(x_digits[i - shift]) for i in range(shift, len(x_digits)))

