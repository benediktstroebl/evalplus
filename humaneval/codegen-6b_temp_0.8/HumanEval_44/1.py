

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
    to_ten = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10}
    if x < 0:
        x = -x
    chars = []
    while x > 0:
        chars.append(str(x % base))
        x = x // base
    chars.reverse()
    return ''.join(chars)
