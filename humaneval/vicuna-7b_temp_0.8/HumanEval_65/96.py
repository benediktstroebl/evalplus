
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    sign = '+'
    if x < 0:
        x = -x
        sign = '-'
    digits = map(int, str(x))
    right_digits = digits[::-1]
    result = ''.join([str(digit)[shift] if sign else str(digit)[-shift] for digit in right_digits])
    return sign + result
