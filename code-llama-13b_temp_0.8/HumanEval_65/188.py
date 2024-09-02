
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # get the length of the number to check shift
    num = len(str(x))

    # reverse the number if shift is greater than number of digits
    if shift > num:
        return str(x)[::-1]

    # otherwise do the shift
    else:
        # split the number into digits
        digits = [int(i) for i in str(x)]

        # do the shift
        shifted = digits[shift:] + digits[:shift]

        # return the result
        return "".join(str(i) for i in shifted)

