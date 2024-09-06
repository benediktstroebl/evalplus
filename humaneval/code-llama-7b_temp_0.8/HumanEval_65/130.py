
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    if len(str(x)) == shift:
        return str(x)[::-1]

    if len(str(x)) < shift:
        return str(x)

    string = str(x)
    reversed_string = string[::-1]
    shift_string = reversed_string[0:shift]
    remaining_string = reversed_string[shift:]

    return shift_string + remaining_string

