

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
    assert 2 <= base <= 10, "Base must be between 2 and 10."
    x_str = str(x)
    if x_str[0] == '-':
        sign = -1
        x_str = x_str[1:]
    else:
        sign = 1
    out = []
    n = len(x_str) - 1
    while n >= 0:
        curr_digit = x_str[n]
        num = int(curr_digit)
        if num < base:
            out.insert(0, num * sign)
        else:
            out.insert(0, num % base * sign)
            # print(num, num % base * sign)
        n = n - 1
    out = list(map(str, out))
    if sign == -1:
        out.insert(0, '-')
    return ''.join(out)
