
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if x < 10:
        return str(x)
    else:
        digits = []
        while x != 0:
            digits.append(x % 10)
            x = x // 10
        n = len(digits) - shift
        return str(digits[n:] + digits[:n])

