

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
    if not 2 <= base <= 9:
        raise ValueError("base must be between 2 and 9, inclusive")

    new_x = []
    while x:
        remainder = x % base
        if remainder < 10:
            new_x.append(str(remainder))
        else:
            new_x.append(chr(ord('A') + remainder - 10))
        x //= base
    new_x.reverse()
    return ''.join(new_x)

