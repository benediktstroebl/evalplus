

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

    numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    remainder_stack = []
    while x > 0:
        remainder = x % base
        remainder_stack.append(remainder)
        x = x // base
    result = ""
    while remainder_stack:
        result = numbers[remainder_stack.pop()] + result
    return result

