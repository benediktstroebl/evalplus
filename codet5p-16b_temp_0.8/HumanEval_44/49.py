

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

    base_list = [str(i) for i in range(base)]
    result = ""
    while x:
        result = base_list[x % base] + result
        x //= base
    return result
