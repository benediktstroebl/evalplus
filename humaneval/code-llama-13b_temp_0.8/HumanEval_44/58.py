

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
    i, ans = x, []
    while i > 0:
        ans.append(str(i % base))
        i //= base
    ans.reverse()
    return ''.join(ans)

