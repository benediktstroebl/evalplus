

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
    if base > 10:
        raise ValueError("Base must be less than 10.")
    if x == 0:
        return ''
    while x >= base:
        x = x // base
        if x != 1:
            yield f'{x}'  # change_base() returns a generator that yields the intermediate strings
    return ''.join(yield)
