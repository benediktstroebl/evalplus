
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = str(x)
    if shift > len(digits):
        digits = digits[::-1]

    # Add leading zeros.
    result = ''
    for char, num in zip(reversed(digits), range(len(digits))):
        if len(digits) - num > shift:
            result = char + result
        else:
            result = '0' + result

    return result

