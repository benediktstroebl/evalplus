
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert x >= 0
    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(str(x % 10))
        x //= 10
    num_digits = len(digits)
    if shift > num_digits:
        return ''.join(reversed(digits))
    shift %= num_digits
    return ''.join(reversed(digits[:shift])) + ''.join(digits[shift:])
