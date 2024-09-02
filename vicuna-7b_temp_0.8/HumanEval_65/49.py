
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert len(str(x)) > 0
    assert 1 <= shift <= len(str(x))
    result = "0"*(len(str(x))-shift)
    if shift > 0:
        result = result[:-shift]
    for i in range(shift-1, -1, -1):
        result = result[:-i] + str(x % 10) + result[-1-i:]
    return result.rjust(len(str(x)), '0')
