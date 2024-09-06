

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
    # Convert x to a string in base 10
    x_str = str(x)
    # Convert x_str to base base
    base_str = "0"
    for i in range(len(x_str)):
        if x_str[i] >= base:
            break
        base_str = base_str + x_str[i]
    # Remove leading zeros
    x_str = x_str[len(base_str):]
    return x_str