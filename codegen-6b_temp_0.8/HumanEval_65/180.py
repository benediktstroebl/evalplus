
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    rev_x = x % 10
    whole_x = x // 10
    result = whole_x * 10 + rev_x
    if shift >= len(str(result)):
        return str(result)[-1::-1]
    return str(result)[len(str(result)) - shift - 1 :: -1]

