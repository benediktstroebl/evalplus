

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
    # convert input number to base 10
    x_10 = str(x)

    # perform the conversion in the specified base
    base_converted = []
    while x_10:
        base_converted.append(x_10[0] if x_10[0] in '0123456789' else 0)
        x_10 = x_10[1:]

    # convert the result back to base 10
    converted = ''.join(str(c) for c in base_converted)

    return converted
