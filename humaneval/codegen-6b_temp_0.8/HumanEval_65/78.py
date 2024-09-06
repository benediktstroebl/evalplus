
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x, shift = int(x), int(shift)
    if x == 0:
        return "0"
    n = 0
    while x > 0:
        shift_digit = x % 10
        x = int(x / 10)
        n = n * 10 + shift_digit
    n = n % 10**(len(str(x))-shift)
    return str(n)
