

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
    if base > 36:
        raise ValueError("Base must be less than 37")
    elif x < 0:
        return "-" + change_base(-x, base)
    elif x == 0:
        return "0"

    num = []
    while x:
        x, digit = divmod(x, base)
        num.append(digits[digit])
    num.reverse()  # reverse the result

    return "".join(num)

