
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    # shift = 1, 23456
    # shift = 2, 3456
    # shift = 3, 456
    # shift = 4, 56
    # shift = 5, 6
    # shift = 6, 12
    # shift = 7, 21

    number_string = str(x)
    number_list = []

    for digit in number_string:
        number_list.append(digit)

    list_length = len(number_list)
    if shift > list_length:
        return ''.join(reversed(number_list))

    number_list = number_list[shift:] + number_list[:shift]

    return ''.join(number_list)

