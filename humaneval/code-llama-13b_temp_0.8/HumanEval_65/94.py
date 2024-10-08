
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if 10**len(str(x)) < x:
        return str(x)[::-1]
    else:
        digits = [int(i) for i in str(x)]
        if shift <= len(digits):
            for _ in range(shift):
                digits.append(digits.pop(0))
            return ''.join([str(i) for i in digits])
        else:
            return circular_shift(x, shift % len(digits))

