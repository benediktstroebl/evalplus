

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
    if x < 0:
        raise ValueError("input number must be greater than 0")
    if base < 2 or base > 256:
        raise ValueError("base must be 2 <= base <= 256")
    converted_string = ""
    while x > 0:
        converted_string += str(x % base)
        x = x // base
    return converted_string[::-1]
