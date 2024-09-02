
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Make a copy of x
    copy = x
    # Make a list that contains the digits of the number
    x_str = [int(i) for i in str(x)]
    # Number of digits
    n = len(x_str)
    # Make a list that will contain the shifted digits
    shifted = []
    # If shift is larger than number of digits
    if shift > n:
        # Reverse the digits and add it to the shifted list
        shifted.extend(x_str[::-1])
    else:
        # Add the last n - shift number of digits to the shifted list
        shifted.extend(x_str[:n - shift])
        # Add the first shift number of digits to the shifted list
        shifted.extend(x_str[n - shift:])
        # Reverse the digits and add it to the shifted list
        shifted.extend(x_str[::-1])
    # Make a string from the shifted digits and return the result
    return str(''.join(map(str, shifted)))
