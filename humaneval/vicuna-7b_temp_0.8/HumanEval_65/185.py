
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = "0" + str(x)
    shifted_digits = []
    while digits:
        n = int(digits[:-1])
        shifted_digits.append(digits[-1])
        digits = digits[1:-1]
    return "".join(reversed(shifted_digits))
