
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # the digits are in a list and each digit is a string
    digits = [str(d) for d in x]
    # reverse the list if the shift is greater than the number of digits
    if shift > len(digits):
        digits = [digits[0], digits[1], digits[2], digits[2], digits[1], digits[0]]
    result = ''.join(digits)
    return result