

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
    # Handle errors in input x and base
    if x < 0 or base < 2:
        return "Error"
    # Create list for conversion and initialize with first digits
    convert = []
    convert.append(x % base)
    x = x // base
    while x > 0:
        convert.append(x % base)
        x = x // base
    # Reverse order of list elements and convert to string
    return ''.join(str(i) for i in reversed(convert))
