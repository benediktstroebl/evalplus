
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    "*** YOUR CODE HERE ***"
    x = str(x)
    if shift <= len(x):
        result = ''
        for i in range(len(x) - shift):
            result += x[i + shift]
        for j in range(shift):
            result += x[j]
    else:
        result = x[::-1]
    return result

