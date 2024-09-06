

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
    # Your code here
    b = string.digits + string.ascii_uppercase[:6]
    if base < 2 or base > len(b):
        raise ValueError("Invalid base.")
    if x < 0:
        sign = "-"
        x = -x
    elif x == 0:
        return "0"
    else:
        sign = ""
    digits = []
    while x:
        digits.append(b[x % base])
        x //= base
    return sign + "".join(reversed(digits))
