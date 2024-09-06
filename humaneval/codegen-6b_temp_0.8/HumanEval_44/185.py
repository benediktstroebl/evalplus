

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
    if x < base:
        return str(x)
    d = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
    return change_base(x//base, base)+d[x%base]
