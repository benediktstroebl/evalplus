
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    sign = ''
    if x < 0:
        x = -x
        sign = '-'
    else:
        sign = ''
    result = '0' * (shift - len(str(x)))
    if len(str(x)) - len(str(result)) > 0:
        result = '0' + result
    if sign:
        result = sign + result
    return result.rjust(len(str(x)), '0')
