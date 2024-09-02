
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    result = str(x)
    if shift < 0:
        shift = abs(shift)
        result = result[:shift] + result[:shift + 1] + result[shift + 1:]
    if len(result) < shift:
        shift = shift - len(result)
        result = result[len(result) - shift:] + result[:len(result) - shift]
    if shift!= 0:
        result = result[-shift:] + result[:-shift]
    return result

