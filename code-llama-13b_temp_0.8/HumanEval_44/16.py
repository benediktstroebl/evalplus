

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
    assert x >= 0, "x is negative."
    assert base > 0, "base is negative."
    assert base <= 10, "base is larger than 10."

    # your code here
    if x < base:
        return str(x)
    else:
        return change_base(x//base, base) + str(x%base)

