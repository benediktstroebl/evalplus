

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
    digits = [str(d) for d in x // (10 ** (n//2)) for n in range(1, len(d.digits))]
    return ''.join(digits[-n:]) + '0' * (n // 2)
