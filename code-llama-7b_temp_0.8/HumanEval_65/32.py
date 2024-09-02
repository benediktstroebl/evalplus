
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
    if x == 0:
        return '0'
    x_str = str(x)
    n = len(x_str)
    digit = x_str[n - 1]
    res = digit
    if shift < n:
        for i in range(n - 1 - shift, -1, -1):
            res += x_str[i]
    else:
        res += digit * (shift // n)
        res += x_str[:n - shift % n]
        res += x_str[:shift % n]
    return res

