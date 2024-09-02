

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
    if base <= 10:
        result = ''
        while x > 0:
            result = str(x % base) + result
            x = int(x / base)
        return result
    else:
        raise ValueError("Base numbers should be less than 10.")

