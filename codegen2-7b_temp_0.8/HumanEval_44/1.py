

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
    if base < 2 or base > 10:
        raise ValueError("Base must be less than 10 and greater than 1")
    if x == 0:
        return "0"
    digits = list("0123456789abcdef")
    reversed_digits = digits[::-1]
    return "".join(reversed_digits[x:x+base])
