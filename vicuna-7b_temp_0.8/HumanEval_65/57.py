
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    num = int(x)
    shift = int(shift)
    if shift < 0:
        raise ValueError("shift should be non-negative")
    if shift > len(str(num)):
        return str(num)[::-1]
    result = ""
    for i in range(0, len(str(num)), shift):
        result = str(num)[i:i+shift] + result
    return result
