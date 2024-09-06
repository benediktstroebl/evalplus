
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = "0123456789"
    result = ""
    while x > 0:
        result = digits[x % 9] + result
        x //= 9
    return result[::-1] if shift > len(result) else result
