

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
        return '0'

    # ord('0') is 48, ord('9') is 57, ord('a') is 97, ord('z') is 122.
    alphabet = '0123456789' + 'abcdefghijklmnopqrstuvwxyz'

    ans = []
    while x > 0:
        ans.append(alphabet[x % base])
        x = x // base
    return ''.join(ans[::-1])

