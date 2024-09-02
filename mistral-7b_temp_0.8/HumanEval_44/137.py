

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base == 10:
        return str(x)
    elif base < 10:
        # Create an empty string to append to
        s = ""
        while x > 0:
            # Get the least significant digit
            d = x % base
            # Append to the string
            s = str(d) + s
            # Get the previous number
            x = x // base
        return s
    else:
        raise ValueError("Base must be less than 10.")
