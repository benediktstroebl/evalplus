
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # create an array of all the digits
    digits = [int(x) for x in str(x)]
    # append digits to the right as many times as we need to shift
    for _ in range(shift):
        digits.append(digits.pop(0))
    # convert the array of digits to a string and return
    return ''.join([str(x) for x in digits])

