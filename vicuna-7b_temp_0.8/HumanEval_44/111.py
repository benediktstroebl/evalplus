

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
    base_digits = [str(digit * (power / base)) if power % base == 0 else digit for digit, power in [
        (x // i + 1, i) for i in range(1, base + 1)
    ]]
    result = ''.join(str(digit) for digit in base_digits)
    return result
