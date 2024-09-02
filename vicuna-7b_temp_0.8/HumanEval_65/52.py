
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = "0"
    for i in range(shift):
        s = s[::-1] + s[1:]
    return s.replace("0", "") + str(int(x/1000000000)) + str(int(x/100000000)) + str(int(x/10000000)) + str(int(x/1000000)) + str(int(x/100000)) + str(int(x/10000)) + str(int(x/1000)) + str(int(x/100)) + str(int(x/10)) + str(int(x))
