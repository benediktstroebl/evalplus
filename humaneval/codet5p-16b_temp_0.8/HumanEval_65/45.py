
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    digits = [int(i) for i in str(x)]
    if shift > len(digits):
        digits = digits[::-1]
    else:
        digits = digits[-shift:] + digits[:-shift]
    return "".join([str(i) for i in digits])
