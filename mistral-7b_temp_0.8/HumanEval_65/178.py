
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    ans = []
    while x != 0:
        ans.append(x % 10)
        x //= 10
    ans = ans[-shift:] + ans[:-shift]
    return ''.join(map(str, ans))
