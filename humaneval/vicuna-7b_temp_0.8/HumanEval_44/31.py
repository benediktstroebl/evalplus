

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
    result = ''
    for i, c in enumerate(str(x)):
        new_c = ord(c) in (ord('0'), ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7'), ord('8'), ord('9'))
        if new_c:
            result += str(ord(c) - ord('0'))
        else:
            result += str(i + 1)
        if i < len(x) - 1:
            result += str(x[i+1])
        if new_c or i == len(x) - 1:
            if i % base == 0:
                break
        else:
            result += str(i % base)
    return result