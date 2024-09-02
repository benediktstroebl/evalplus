
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # your code here
    s = list(str(x))
    s.reverse()
    for i in range(len(s)):
        x = s.pop()
        s.insert(shift%len(s), x)
    return ''.join(s)

