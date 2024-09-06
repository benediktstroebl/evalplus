

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
    digits = "0123456789"
    result = []

    if base > len(digits):
        return "Invalid Base"

    while x > 0:
        result.append(digits[x % base])
        x //= base

    return "".join(reversed(result))
