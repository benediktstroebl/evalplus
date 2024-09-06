

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
    assert x >= 0, "x must be >= 0"
    assert 0 < base < 10, "base must be 1 < base < 10"

    num = x
    lst = []
    while num > 0:
        lst.append(num % base)
        num //= base

    # num_str = ''.join(str(num) for num in lst)
    # num_str = ''.join(map(str, lst))
    num_str = ''.join([str(x) for x in lst])
    return num_str

