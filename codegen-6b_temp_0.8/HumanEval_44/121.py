

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
    if x < 0:
        return change_base(abs(x), base)
    # multiply one by base**(digit)
    digit = 0
    res = 1
    while x >= 1:
        digit += 1
        res *= base
        x -= 1
    output_base = []
    while res != 0:
        res, dig = divmod(res, base)
        output_base.append(chr(dig + ord('0')))
    output_base.reverse()
    return ''.join(output_base)
