

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
    if x == 0:
        return 0
    digit = 0
    ans = ''
    while x > 0:
        digit = x % base
        if digit > 9:
            ans += chr(digit + 55)
        else:
            ans += str(digit)
        x = x // base
    return ans[::-1]

