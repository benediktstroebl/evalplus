

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

    if base > 10 or base < 2:
        raise ValueError("Base is not less than 10 or bigger than 1.")
    result = ""
    while x > 0:
        result = str(x % base) + result
        x //= base
    return result

