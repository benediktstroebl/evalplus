
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # the number of digits
    num_digits = len(str(x))
    # find the number of digits to shift to the right
    shift_right = shift % num_digits
    # if shift > num_digits, shift the digits left
    if shift_right == 0:
        return str(x)
    # split the number into a list of digits
    digits = [int(i) for i in str(x)]
    # remove the last num_digits - shift_right digits
    digits = digits[:-shift_right]
    # insert the remaining digits to the beginning
    digits = digits[-shift_right:] + digits
    # return the list as a string
    return "".join([str(i) for i in digits])

