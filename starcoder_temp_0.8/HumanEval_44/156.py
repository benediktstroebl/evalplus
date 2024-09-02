

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
    if base == 10:
        return str(x)
    elif base <= 10:
        temp = ''
        while x!= 0:
            temp += str(x % base)
            x = x // base
        temp = temp[::-1]
        return temp
    else:
        return 'Base cannot be greater than 10'
