

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

    base_num = [0 for _ in range(len(change_base(x, base)[0]))]
    for i, digit in enumerate(change_base(x, base)):
        base_num[-i - 1] = int(digit)
    return ''.join(map(str, base_num))

