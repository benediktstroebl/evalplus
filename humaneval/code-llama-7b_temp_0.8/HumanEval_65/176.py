
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert shift >= 0
    s = str(x)
    result = []
    for i in range(shift):
        result.append(s[i])
    for i in range(shift, len(s)):
        result.append(s[i - shift])
    return "".join(result)

