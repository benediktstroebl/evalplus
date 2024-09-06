
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = '0'
    while shift > 0:
        # get the shifted digit
        digit = digits[shift-1]
        # add the next digit to the left end of the string
        digits = digits[:-1] + '0' + digits[-1]
        shift -= 1
    return ''.join(reversed(digits))
