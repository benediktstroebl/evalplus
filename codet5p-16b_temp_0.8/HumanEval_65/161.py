
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    from math import log
    num_digits = int(log(x, 10)) + 1
    new_num = ""

    if shift > num_digits:
        return circular_shift(str(x), num_digits)

    else:
        for digit in str(x):
            new_num += str(digit)

        new_num = new_num[-shift:] + new_num[:-shift]
        return new_num
