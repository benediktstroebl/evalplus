
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
    if num_digits == 0:
        return ""
    if shift == 0:
        return str(x)
    if shift < 0:
        return circular_shift(x, num_digits+shift)
    if shift > num_digits:
        return circular_shift(x, shift-num_digits)
    first_digit = x // 10**(num_digits-shift)
    rest_of_number = x % 10**(num_digits-shift)
    return str(rest_of_number) + str(first_digit)
