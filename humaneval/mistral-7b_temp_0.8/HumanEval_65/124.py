
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    ans = ""
    str_x = str(x)
    for c in str_x:
        ans = c + ans
    if shift > len(str_x):
        return ans[::-1]
    else:
        return ans[shift:] + ans[:shift]

