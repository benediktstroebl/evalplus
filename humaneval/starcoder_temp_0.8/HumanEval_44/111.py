

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
    # first step check if the base is a valid number.
    if base < 2 or base > 10:
        raise ValueError(f'base number should be less than 10 and greater than 1')
    # convert x to string
    x = str(x)
    # base conversion process
    ans = ''
    while x!= '':
        y = x[-1]
        x = x[:-1]
        ans = ans + chr(ord('0') + int(y, 10) - int(y, base))
    return ans[::-1]
