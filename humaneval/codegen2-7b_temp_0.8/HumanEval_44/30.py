

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
    if base <= 10:
        raise ValueError("base should be greater than 10")
    if base == 10:
        return str(x)
    
    x_string = str(x)
    return "".join(list(map(lambda char: char + str(x_string), 
                           list(range(10, 0, -1))[:base]
