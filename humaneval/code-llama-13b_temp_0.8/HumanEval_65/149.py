
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    n = str(x)
    if len(n) == 1:
        return n
    elif len(n) > 1 and shift > 0:
        a = int(n[-1])
        n = n[:-1]
        return str(a) + n
    elif len(n) > 1 and shift > len(n):
        return n[::-1]
    
    
