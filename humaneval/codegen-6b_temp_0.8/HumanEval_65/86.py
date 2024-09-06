
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x %= 10**(len(str(x)) - 1)

    # convert to string and rotate each digit backwards
    str_number = str(x)[::-1]
    return str(int(str_number[:shift])) + str(int(str_number[shift:]))

