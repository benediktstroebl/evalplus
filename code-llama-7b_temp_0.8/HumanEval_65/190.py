
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # the while loop could be replaced with the following list comprehension:
    # return ''.join([str((x % 10 + shift) % 10) for x in reversed(str(x))])
    x_str = str(x)
    result = ''
    while x != 0:
        x, d = divmod(x, 10)
        result += str((d + shift) % 10)
    return result or x_str
    
    

