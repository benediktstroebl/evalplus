
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    sign = 1 if x < 0 else 0
    result = ""
    for i in range(len(str(x))):
        result = str(int(x) % 10) + result
        x = int(x / 10)
    return sign + result
