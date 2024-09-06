
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Ensure that shift is valid
    shift %= len(str(x))

    # reverse digits if shift is to the left                         
    if shift > 0:
        digits = str(x)[::-1]
    else:
        digits = str(x)

    # remove leading zeros
    digits = digits.lstrip('0')

    # add leading 0(s) to digits if shift is to the right                      
    if abs(shift) > len(digits):
        add_zeros = abs(shift) - len(digits)
        digits = '0' * add_zeros + digits

    # shift the digits                                             
    digits = str(int(digits[shift:] + digits[:shift]))

    print(digits)
    return digits
