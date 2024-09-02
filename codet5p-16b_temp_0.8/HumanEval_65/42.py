
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
    if shift > len(str(x)):
        for i in str(x)[::-1]:
            result += str(i)
        return result
    else:
        for i in str(x)[::-1][:shift][::-1]:
            result += str(i)
        for i in str(x)[::-1][shift:]:
            result += str(i)
    return result
