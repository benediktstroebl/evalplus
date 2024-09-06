
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert 0 <= shift <= len(x)
    n = len(x)
    if shift > n:
        return str(int(x[n - 1]) + int(x[0:n - 1]))[-1::-1]
    return str(int(x) >> shift)[-1::-1] + str(int(x) << shift)[:n - shift]

