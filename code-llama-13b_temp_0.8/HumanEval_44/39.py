

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
    new_base_rep = []
    while x > 0:
        remainder = x % base
        x = x // base
        new_base_rep.append(remainder)
    for i in range(len(new_base_rep)):
        new_base_rep[i] = str(new_base_rep[i])
    new_base_rep.reverse()
    return ''.join(new_base_rep)
