
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    string = str(x)
    list = []
    if len(string) > shift:
        return string[shift:] + string[:shift]
    else:
        for i in range(0,len(string)):
            list.append(string[-i])
        return "".join(list)

    # """
    # Using slicing
    # if shift > len(string):
    #     return string[::-1]
    # return string[shift:] + string[:shift]
    # """

    """
    Using split, join and reversed
    if shift > len(string):
        return "".join(reversed(string))
    return string[shift:] + string[:shift]
    """

    """
    Using len, split, join, reversed and slicing.
    if shift > len(string):
        return "".join(reversed(string))
    return string[-shift:] + string[:-shift]
    """

