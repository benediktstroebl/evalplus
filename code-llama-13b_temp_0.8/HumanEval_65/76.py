
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    original = str(x)
    reversed = ""
    if len(original) < shift:
        for index in range(shift):
            reversed += original[index]
        return reversed
    else:
        for index in range(len(original) - shift, len(original)):
            reversed += original[index]
        for index in range(len(original) - shift):
            reversed += original[index]
        return reversed

