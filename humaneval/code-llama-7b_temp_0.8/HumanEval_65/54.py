
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = []
    while x > 0:
        digits.append(str(x % 10))
        x = x // 10
    if len(digits) <= shift:
        return ''.join(reversed(digits))
    return ''.join(digits[-shift:]) + ''.join(reversed(digits[:-shift]))
