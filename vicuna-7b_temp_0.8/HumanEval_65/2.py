
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # handle negative shift
    if shift < 0:
        shift = abs(shift)
        x = -x if x >= 0 else -(-x)
        shift = -shift
        
    # handle special case of zero shift
    if shift == 0:
        return "0" + str(x)
    # handle special case of one shift
    elif shift == 1:
        return str(x)[2:].zfill(2)
        
    # handle general case
    n = len(str(x))
    result = "0"
    for i in reversed(range(shift)):
        result += str(x[n-i-1])
        n -= i
    if n > 0:
        result += str(x[n-1])
    return result
