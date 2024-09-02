

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
    if base < 2 or base > 10:
        raise ValueError("base must be between 2 and 10")
    else:
        digits = string.digits + string.ascii_lowercase
        base10_num = 0
        for i, digit in enumerate(str(x)[::-1]):
            base10_num += digits.index(digit) * base ** i
        return base10_num
