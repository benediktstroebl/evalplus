

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

    digits = []
    x_copy = x
    while x_copy > 0:
        x_copy, r = divmod(x_copy, base)
        digits.append(r)
    return change_base_helper(''.join(str(d) for d in digits), base)

