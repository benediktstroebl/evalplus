
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
        return x
    if shift < 0:
        return reverse_digits(x)
    l = [None]*len(str(x))
    for i in range(len(l)):
        l[(i + shift) % len(l)] = x % 10
        x //= 10
    return "".join(map(str, l))

