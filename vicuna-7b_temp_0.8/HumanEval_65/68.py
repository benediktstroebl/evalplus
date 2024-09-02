
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    digits = list(map(str, x))
    reversed_digits = digits[::-1]
    result = "".join(reversed_digits[::-1])
    while shift > 0:
        result = "".join([result[-shift:], result[:-shift]])
        shift = shift - 1
    return result
