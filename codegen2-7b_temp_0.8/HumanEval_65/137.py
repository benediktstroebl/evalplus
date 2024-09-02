
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
    else:
        digits = str(x)
        output = [x]
        for i in range(1, shift):
            output.append(int(digits[-1]) * 10 + int(digits[-2]))
            digits = digits[:-1]
        return ''.join(output
