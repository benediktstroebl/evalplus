
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    result = ""
    # iterate through the string representation of x
    for i in range(len(x)):
        # get the index of the i-th digit
        index = (i + shift) % len(x)
        # append the i-th digit to the result
        result += x[index]
    return result
