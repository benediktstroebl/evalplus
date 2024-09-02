

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
    def to_base_n(num: int, n: int):
        base_num = []
        while num > 0:
            mod = num % n
            num = num // n
            base_num.insert(0, mod)
        return base_num
    if base > 10:
        raise ValueError('the base should be less than 10')
    return str(to_base_n(x, base))
