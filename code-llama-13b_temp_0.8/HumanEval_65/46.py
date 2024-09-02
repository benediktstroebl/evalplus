
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    num_digits = len(str(x))
    if shift > num_digits:
        shift = shift - num_digits
    number = str(x)
    left_part = number[:num_digits - shift]
    right_part = number[num_digits - shift:]
    result = right_part + left_part
    return result

