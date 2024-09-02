
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # A. Find the number of digits in the integer x, and loop through them.
    x_str = str(x)
    x_len = len(x_str)

    # B. Use modulo to get the remainder of shift//x_len
    # C. If the remainder is 0, then the number of digits shifted is 0
    # D. If the remainder is not 0, then shift is less than the number of digits
    # E. If shift is less than the number of digits, loop through the digits
    # F. If shift is greater than the number of digits, loop through the digits in reverse order

    if shift % x_len == 0:
        x_str = x_str[::-1]
        return x_str
    else:
        x_str = x_str[shift % x_len:] + x_str[:shift % x_len]
        return x_str
