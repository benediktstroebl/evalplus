

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
    if base > 36 or base < 2:
        raise Exception("Base has to be between 2 and 36.")
    return "".join([chr(x%base+48) if x > 9 else chr(x+48) for x in range(base)
