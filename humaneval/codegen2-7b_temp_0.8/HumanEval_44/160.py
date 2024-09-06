

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
    d = {2: '01', 3: '111', 4: '1111', 5: '11111', 6: '111111', 7: '1111111'}
    return ''.join(map(lambda y: d[base][y], str(x).zfill(base)))
