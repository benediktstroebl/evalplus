

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
        raise ValueError("base should be between 2 and 10")

    number_str = str(x)
    return number_str.replace("0b", "") + "0" * (10 - len(number_str)) + "b" + number_str.replace("0x", "") + "0" * (16 - len(number_str
