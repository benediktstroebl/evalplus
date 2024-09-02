

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
    assert base >= 2
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_base_list = []
    while x > 0:
        remainder = x % base
        x = x // base
        new_base_list.insert(0, digits[remainder])
    return "".join(new_base_list)
