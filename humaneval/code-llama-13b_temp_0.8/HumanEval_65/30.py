
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # x_list = [i for i in str(x)]
    # x_list.reverse() if shift > len(str(x)) else x_list[-shift:] + x_list[:-shift]
    # return ''.join(x_list)

    return str(x)[-shift:] + str(x)[:-shift] if shift < len(str(x)) else str(x)[::-1]

