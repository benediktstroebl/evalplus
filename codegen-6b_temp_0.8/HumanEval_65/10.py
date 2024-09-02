
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # make shift a string of length len(x) by adding leading zeros
    shift = str(shift)
    if len(shift) > len(x):
        shift = '0'*(len(x)-len(shift)) + shift
    # compute the integer in a Python slice
    integer = x//10**(len(x)-1) + x%10**(len(x)-1)//10
    # compute the remainder
    remainder = integer + int(shift[:1])
    if remainder > 9:
        remainder %= 10
    else:
        remainder = int(shift)
    # compute the new integer
    x = integer*10**(len(x)-1) + remainder
    return str(x)

