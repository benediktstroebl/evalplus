

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
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, f'base is out of range: {base}'
    convert_string = string.digits + string.ascii_lowercase
    result = ''
    while x > 0:
        result = convert_string[x % base] + result
        x //= base
    return result
