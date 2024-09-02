
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert shift > 0, "shift must be > 0"
    assert 0 < x < 10**9, "x must be an integer between 0 and 10**9"
    result = ""
    for digit in str(x):
        result = digit + result
        if result[-shift:] == str(x):
            result = result[:shift]
        else:
            result = result[:shift] + str(x)
