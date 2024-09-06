
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    num_str = str(x)
    num_length = len(num_str)
    if shift >= num_length:
        return num_str[::-1]
    else:
        # Grab the last shift characters
        num_left = int(num_str[:shift])
        # Grab the remaining characters
        num_right = int(num_str[shift:])
        # Add num_right to the left of num_left
        return str(num_right) + str(num_left)
