
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # get length of number in string
    len_str = len(str(x))

    # shift the number
    shifted_num = (int(str(x)[-shift:]) + int(str(x)[:-shift])) % 10**(len_str)

    # return string version of shifted_num
    return str(shifted_num)
