
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift == 0:
        return str(x)
    else:
        result = str(x)
        remaining_shift = shift % len(result)
        result = result[remaining_shift:] + result[:remaining_shift]
        return result
