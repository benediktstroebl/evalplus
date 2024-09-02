
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert isinstance(x, int), 'input is not of type int'

    if shift > x:
        shift = shift % x

    n = len_digits(x)
    res = ''

    for i in range(n):
        p = (i + shift) % n
        res += str(x % 10)
        x //= 10
        if p == 0:
            p = n

    return res[::-1] if shift < n else res
