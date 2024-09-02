
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # the number of digits of x
    digits_x = len(str(x))
    # the number of digits of the circular shift of x
    digits_shift = digits_x - shift if shift < digits_x else 0
    # return str(x)[digits_x-digits_shift:] + str(x)[:digits_x-digits_shift]
    return str(x)[digits_x-digits_shift:] + str(x)[:digits_x-digits_shift][::-1]
