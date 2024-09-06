
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    string_number = str(x)
    number_of_digits = len(string_number)
    if number_of_digits <= 1:
        return string_number
    if shift >= number_of_digits:
        shift = shift % number_of_digits
        return string_number[number_of_digits - shift :] + string_number[: number_of_digits - shift]
    return string_number[number_of_digits - shift :] + string_number[: number_of_digits - shift]

