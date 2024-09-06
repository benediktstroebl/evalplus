

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
    lower_base = 0
    higher_base = 1
    final_base = ""
    while True:
        if lower_base < base:
            if x < base**lower_base:
                final_base = "0" + final_base
                break
            x -= base**lower_base
            final_base += str(x)
            lower_base += 1
        else:
            if x < base:
                final_base = str(x) + final_base
                break
            x -= base**lower_base
            final_base += str(x)
            lower_base += 1
    return final_base

