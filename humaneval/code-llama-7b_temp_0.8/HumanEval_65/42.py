
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    def reverse(x):
        rev = ""
        while x > 0:
            rev = str(x % 10) + rev
            x = x // 10
        return rev

    if not x:
        return str(x)
    elif x < 0:
        return "-" + reverse(-x)
    else:
        rev = reverse(x)
        if shift > len(rev):
            return rev
        return rev[:-shift] + rev[-shift:]

