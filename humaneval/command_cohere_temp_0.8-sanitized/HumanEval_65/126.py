def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    """
    x = str(x)
    front, back = x[:shift], x[shift:]
    return f"{back}{front}" if shift < len(x) else f"{x[::-1]}"