
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    original_digits = [int(digit) for digit in str(x)]

    if len(original_digits) <= shift:
        return ''.join(str(i) for i in original_digits[::-1])
    else:
        return ''.join(str(i) for i in original_digits[-shift:]) + ''.join(str(i) for i in original_digits[:-shift])

