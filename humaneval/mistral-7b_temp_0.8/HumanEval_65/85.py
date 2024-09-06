
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # digits is the list of the digits
    digits = []
    while x > 0:
        digits.append(x%10)
        x = x//10
    # if shift > the number of digits in digits
    # return the string of the digits reversed
    if shift > len(digits):
        return str(digits[::-1])
    elif shift == len(digits):
        return str(digits)
    else:
        # Shift all the digits in the list right by shift
        for i in range(shift):
            digits.append(digits[0])
            del digits[0]
        return str(digits)
