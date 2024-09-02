

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
    if base < 2 or base > 9:
        raise ValueError("base should be 2-9")
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if x == 0:
        return digits[base - 1]
    result = ""
    while x > 0:
        remainder = x % base
        result = digits[remainder] + result
        x = x // base
    return result

