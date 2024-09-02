

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
    assert 1 <= base <= 10, f"{base} is not a base in range 1 <= base <= 10"

    new_value = ''
    while x > 0:
        new_value = str(x % base) + new_value
        x = x // base
    return new_value
