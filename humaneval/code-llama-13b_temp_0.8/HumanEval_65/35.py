
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    number = str(x)
    shifted = ""
    if shift > len(number):
        shift = shift - len(number)
        for i in range(len(number) - 1, -1, -1):
            shifted = shifted + number[i]
    else:
        for i in range(len(number) - shift, len(number)):
            shifted = shifted + number[i]
        for i in range(0, len(number) - shift):
            shifted = shifted + number[i]
    return shifted

