

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
    number = x
    digits = []
    while number != 0:
        digits.append(str(number % base))
        number = number // base
    if number == 0:
        return ''.join(digits[::-1])
    else:
        return ''.join(digits[::-1] + '0' * (base-len(digits)))

