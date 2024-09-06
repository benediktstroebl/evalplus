
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Shift by 1 digit at a time.
    result = str(x)
    if shift <= 0:
        return result[::-1]
    while shift > 0:
        result = circular_shift_1_digit(result)
        shift -= 1
    return result
