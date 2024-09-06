
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    number_of_digits = str(x)
    if shift >= len(number_of_digits):
        return number_of_digits[::-1]
    else:
        return number_of_digits[-shift:] + number_of_digits[:-shift]
