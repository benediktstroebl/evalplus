

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
    # pre-condition
    assert base < 10
    assert x >= 0
    
    # post-condition
    assert change_base(x, base) == bin(x)[2:]
    assert change_base(x, base) == oct(x)[2:]
    assert change_base(x, base) == hex(x)[2:]
    
    if x < base:
        return str(x)
    else:
        return change_base(x//base, base) + str(x%base)
