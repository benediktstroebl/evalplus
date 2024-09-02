

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
    if base <= 1 or base > 16:
        raise Exception("Invalid base: {}".format(base))

    if x < 0:
        return "-" + change_base(-x, base)

    if x == 0:
        return "0"

    base_characters = "0123456789ABCDEF"
    result = ""
    while x > 0:
        result = base_characters[x % base] + result
        x //= base

    
