
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    return_str = ""
    num_digits = len(str(x))
    # Empty string
    if num_digits == 0:
        return ""
    # Number of digits < shift
    elif num_digits < shift:
        shift = num_digits
    # Reverse
    if shift == num_digits:
        return str(x)[::-1]
    else:
        for i in range(0, shift):
            return_str += str(x)[num_digits - shift + i]
        for i in range(shift, num_digits):
            return_str += str(x)[i]
    return return_str

