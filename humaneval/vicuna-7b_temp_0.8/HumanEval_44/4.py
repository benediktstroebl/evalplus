

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
    digits = [0] * 10
    reversed_digits = [str(x) for x in digits[::-1]]
    reversed_digits = [d if d not in [0,1,2,3,4,5,6,7,8,9] else str(int(d) % base) for d in reversed_digits]
    x = sum([int(d) for d in reversed_digits])
    result = ''
    while x > 0:
        x, y = divmod(x, base)
        result = str(y) + result
    return result
