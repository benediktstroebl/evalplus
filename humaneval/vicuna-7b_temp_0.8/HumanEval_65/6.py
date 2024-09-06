
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    num = int(x)
    if shift >= num:
        shift %= num
        return str(num)[:-shift] + str(num % 10)[-shift:]
    return "".join(str(n) for n in x)[:-shift]
