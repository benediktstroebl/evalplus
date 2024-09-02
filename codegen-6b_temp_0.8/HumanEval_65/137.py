
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    d_string = str(x)
    d_len = len(d_string)
    start = shift % d_len
    reverse = ""
    for i in range(d_len):
        reverse += d_string[(i + start) % d_len]
    return reverse
