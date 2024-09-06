
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x_digits = [int(d) for d in str(x)]
    result = ""
    for i in range(len(x_digits) - shift):
        result = x_digits[i] + result
    for j in range(shift):
        result = "0" + result
    return result
