

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
    if base < 2 or base > 10:
        raise ValueError("Invalid base")
    if x == 0:
        return "0"
    ans = ""
    while x > 0:
        ans = chr(x % base + ord('0')) + ans
        x = x // base
    return
