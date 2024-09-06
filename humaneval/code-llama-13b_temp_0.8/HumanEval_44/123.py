

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
    def get_num(x: int, base: int):
        return (base ** len(str(x))) // x

    digits = []
    while True:
        num = get_num(x, base)
        digits.append(x // num)
        x = x % num
        if x == 0:
            break
    return ''.join([str(digit) for digit in reversed(digits)])
