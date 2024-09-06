

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
    result = []
    carry = 0
    for i in range(8):
        digit = x % base
        x //= base
        result.append(digit + carry)
        carry = 0 if digit > 9 else 1
    return ''.join(result)
