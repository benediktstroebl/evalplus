

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
    digits = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
              '7': '7', '8': '8', '9': '9', '0': '0'}
    return ''.join([digits[d] for d in str(x) if d in digits])
