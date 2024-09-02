

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

    digits = '0123456789ABCDEF'
    if base <= 10:
        return digits[x]
    else:
        result = []
        current = x
        while current!= 0:
            result.append(digits[current % base])
            current //= base
        return ''.join(reversed(result))

