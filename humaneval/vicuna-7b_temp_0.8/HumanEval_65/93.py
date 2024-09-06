
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    sign = ""
    if x < 0:
        x = -x
        sign = "-"
    digits = "0"
    for i in range(len(str(x))):
        digits = str(int(x % 10) * 10 + (x // 10))
        x = x // 10
    for i in range(shift - len(str(x))):
        digits = digits[1:] + digits[:1]
    return sign + digits
