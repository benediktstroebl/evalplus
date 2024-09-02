

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
    if base < 10:
        digits = []
        while x != 0:
            digits.append(x % base)
            x = x // base
        return ''.join(map(str, digits[::-1]))
    else:
        raise ValueError("Base must be less than 10.")

