

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
    answer = []
    if base > 10:
        return 'Error'
    while x >= base:
        answer.append(str(x // base))
        x = x % base
    answer.append(str(x))
    answer.reverse()
    return ''.join(answer)

