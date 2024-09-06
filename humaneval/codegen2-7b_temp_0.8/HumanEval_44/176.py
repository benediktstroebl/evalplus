

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
    base_dict = {10: "01", 16: "0123456789ABCDEF"}
    x = str(x)
    x_out = ""
    for digit in x:
        x_out += base_dict[base].replace(digit, "")
    return x_out

