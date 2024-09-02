
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    number_str = str(x)
    result = []
    while len(number_str) > shift:
        result.append(number_str[-shift:])
        number_str = number_str[:-shift]
    return ''.join(result + list(reversed(number_str)))
