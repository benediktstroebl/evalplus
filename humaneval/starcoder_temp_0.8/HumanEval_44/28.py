

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
    base_numbers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_x = []
    while x > 0:
        new_x.append(x % base)
        x //= base
    new_x.reverse()
    new_x = "".join([base_numbers[i] for i in new_x])
    return new_x
