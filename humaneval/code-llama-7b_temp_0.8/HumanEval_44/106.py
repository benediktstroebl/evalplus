

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

    def int_to_str(x: int):
        x_str = str(x)
        return x_str

    def str_to_int(x: str):
        x_int = int(x)
        return x_int

    # 10 is the base of decimal number system.
    number_system = int(x)
    x_str = int_to_str(number_system)
    x_int = str_to_int(x_str)
    count = 0
    res = ''
    while x_int > 0:
        res = str(x_int % base) + res
        x_int = x_int // base
        count += 1
    return res

