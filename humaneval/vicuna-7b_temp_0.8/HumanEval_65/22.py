
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = [str(digit) for digit in x]
    result = "".join(reversed(digits))
    while shift > 0:
        if "0" in result:
            shift -= 1
            result = "".join(digits)
        else:
            result = "".join(str(digit) for digit in reversed(digits))
            shift -= 1
    return result