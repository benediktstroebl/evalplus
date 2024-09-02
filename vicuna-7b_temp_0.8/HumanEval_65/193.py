
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Handle the special case of a shift of zero
    if shift == 0:
        return "0" + str(x)

    # Handle the special case of a negative shift
    if shift < 0:
        shift = -shift
        x = -x

    # Determine the number of digits to shift
    shift_digits = shift // len(str(x))

    # Shift the digits right
    shifted = "0" * len(str(x))
    for i in range(shift_digits):
        shifted += str(x % 10)
    x %= 10

    # Append the last digit and return the result
    return shifted[::-1] + x
