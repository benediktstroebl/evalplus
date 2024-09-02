
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    str1 = str(x)
    if len(str1) <= 1 or shift == 0:
        return str1

    if shift < len(str1):
        return str1[shift:] + str1[:shift]
    else:
        return str1[::-1]

