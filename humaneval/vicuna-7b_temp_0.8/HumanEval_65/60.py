
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift <= len(str(x)) % shift:
        result = "".join([str(int(d)) * shift for d in str(x)])
    else:
        result = "".join([str(int(d)) for d in str(x)])
        for i in range(shift - len(str(x)) % shift):
            result = "0" + result
        result = "".join([int(d) for d in result])
    return result.rjust(shift, '0')