

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
    if not isinstance(x, int):
        raise TypeError("Only integer supported.")
    if not isinstance(base, int):
        raise TypeError("Only integer supported.")
    if base <= 1 or base >= 10:
        raise ValueError("Base must be between 2 to 9")

    nums = '0123456789ABCDEF'
    result = ''
    if x < 0:
        x = -x
        result += '-'

    while x != 0:
        result += nums[x % base]
        x //= base

    return result[::-1]

