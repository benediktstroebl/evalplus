

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
    assert base <= 10, "Base must be less than or equal to 10."
    assert base > 0, "Base must be greater than zero."
    assert x >= 0, "Input number must be greater than or equal to 0."
    result = ''
    while x > 0:
        result = str(x % base) + result
        x //= base
    return result

