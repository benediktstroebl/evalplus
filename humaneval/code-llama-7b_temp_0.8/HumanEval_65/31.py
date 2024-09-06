
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift < 1:
        return str(x)
    digits = [int(digit) for digit in str(x)]
    n_digits = len(digits)
    new_digits = digits[shift:] + digits[:shift]
    if n_digits > len(new_digits):
        new_digits.reverse()
    return ''.join([str(x) for x in new_digits])
