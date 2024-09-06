
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    # represent the number as a list
    num_list = [int(x) for x in str(x)]

    # if the shift is greater than the number of digits
    if shift > len(num_list):
        # reverse the number
        return "".join(reversed([str(x) for x in num_list]))
    else:
        # circular shift by shifting the list
        return str(int("".join([str(x) for x in num_list[shift:]] + num_list[:shift])))

    # return the circular shifted number
