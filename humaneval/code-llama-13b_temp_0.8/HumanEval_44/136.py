

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
    # Your code here

    assert base > 0 and base < 10, 'Base must be between 1 and 9'

    remainder = x
    b = ''

    while remainder > 0:
        remainder, mod = divmod(remainder, base)
        b = str(mod) + b

    return b
