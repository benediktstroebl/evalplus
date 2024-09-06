
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert len(str(x)) == 10
    if shift <= 0:
        return str(x)
    else:
        # handle the case of negative shift
        x = str(abs(x))
        reversed = False
        if x[0] in '12':
            reversed = True
        shift = min(shift, 9)
        for i in range(9):
            x = x[:-1] + x[1:] + x[:-i]
            if reversed:
                x = x[::-1]
            if shift == 0:
                break
            shift -= 1
        return str(x)
