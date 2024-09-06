

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
    if x < 0 or base < 1 or base > 9:
        return "invalid input"

    result = ""
    while x > 0:
        result += str(x % base)
        x //= base

    return result[::-1]

