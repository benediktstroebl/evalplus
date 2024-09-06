
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # convert x to a string
    x_str = str(x)
    # shift the digits right
    result_str = ""
    for i in range(0, len(x_str), 3):
        result_str += x_str[i:i+3]
    # reverse the digits
    for i in range(0, len(result_str), 3):
        result_str = result_str[:i] + str(int(result_str[i:])) + result_str[i+1:]
    return result_str