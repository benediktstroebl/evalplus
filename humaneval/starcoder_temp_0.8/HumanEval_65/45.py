
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digit_list = list(str(x))
    if shift > len(digit_list):
        shift = shift % len(digit_list)
        digit_list = digit_list[::-1]
    return "".join(digit_list[shift:] + digit_list[:shift])

