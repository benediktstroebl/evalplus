
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    n = len(str(x))
    result = ""
    for i in range(n, -1, -1):
        result = str(int(result) + (x % 10) * 10 ** (n-i-1))
        x = x // 10
    return result + str(x % 10)