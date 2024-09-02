
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Your code here
    if shift < 0:
        shift = 0
    if shift == 0:
        return x
    elif shift > 0:
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10
        return str(result)[-shift:] + str(result)[:-shift]
    else:
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10
        return str(result)[-shift:] + str(result)[:-shift]
