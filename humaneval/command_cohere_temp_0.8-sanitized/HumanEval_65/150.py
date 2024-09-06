def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    x = str(x)
    x = x[::-1] if shift > len(x) else x[len(x) - shift:] + x[:len(x) - shift]
    return x