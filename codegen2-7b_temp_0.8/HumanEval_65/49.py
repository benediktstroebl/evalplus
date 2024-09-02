
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = [int(digit) for digit in str(x)]
    for i in range(shift):
        if len(digits) > 1:
            digits = digits[1:] + [digits[0]]
        else:
            digits = [0] + digits
    return "".join(map(str, digits
