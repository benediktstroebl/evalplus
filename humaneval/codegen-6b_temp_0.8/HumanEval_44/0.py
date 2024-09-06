

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
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = x
    if x < 0:
        return "-" + change_base(-x, base)
    if x == 0:
        return "0"
    digits = digits[::-1]
    digits_in_base = []
    while n > 0:
        digits_in_base.append(digits[int(n % base)])
        n = int(n / base)

    return "".join(digits_in_base)

