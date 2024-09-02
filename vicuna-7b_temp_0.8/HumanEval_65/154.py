
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift < 0:
        shift += 9
    digits = '0' + str(x)
    result = ''
    for i in range(10):
        if digits[i] == '0':
            result += digits[i+shift]
        else:
            result += digits[i]
    return result
