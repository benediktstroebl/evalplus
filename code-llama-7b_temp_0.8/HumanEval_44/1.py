

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

    nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    base_num = 0
    for i, char in enumerate(reversed(str(x))):
        base_num += int(char) * (base ** i)

    return nums[base_num]

