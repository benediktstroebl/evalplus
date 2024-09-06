
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    str1 = ""
    while x > 0:
        str1 = str1 + str(x % 10)
        x = x // 10

    if shift > len(str1):
        shift = shift % len(str1)
        for i in range(shift):
            str1 = str1[1:] + str1[0]
    else:
        for i in range(shift):
            str1 = str1[1:] + str1[0]
    return str1


