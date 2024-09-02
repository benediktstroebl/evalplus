
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    digits = '0123456789'
    if shift > len(str(x)):
        shift = shift % len(str(x))
    x = str(x)
    new_x = ''
    for i in x:
        index = int(i) + shift
        if index > 9:
            index -= 10
        new_x += digits[index]
    return new_x
