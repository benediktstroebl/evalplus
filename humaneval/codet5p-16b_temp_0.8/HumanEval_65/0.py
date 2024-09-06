
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    number_of_digits = len(str(x))
    if shift <= number_of_digits:
        new_number = str(x)[number_of_digits - shift:] + str(x)[:number_of_digits - shift]
    else:
        new_number = str(x)[number_of_digits - shift:] + str(x)[:number_of_digits - shift] + str(x)[:shift]
    return new_number
