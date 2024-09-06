
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if shift == 0:
        return str(x)
    digit_count = 0
    output = []
    while shift > digit_count:
        output.append(x % 10)
        x //= 10
        digit_count += 1
    output.append(x)
    return "".join(str(d) for d in output[::-1
