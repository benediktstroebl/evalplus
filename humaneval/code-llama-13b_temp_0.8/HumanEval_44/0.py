

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
    b = ""
    #base = 10
    if x == 0:
        return "0"
    while x > 0:
        if x % base == 9:
            b += "9"
            x -= 9
        elif x % base == 8:
            b += "8"
            x -= 8
        elif x % base == 7:
            b += "7"
            x -= 7
        elif x % base == 6:
            b += "6"
            x -= 6
        elif x % base == 5:
            b += "5"
            x -= 5
        elif x % base == 4:
            b += "4"
            x -= 4
        elif x % base == 3:
            b += "3"
            x -= 3
        elif x % base == 2:
            b += "2"
            x -= 2
        elif x % base == 1:
            b += "1"
            x -= 1
        elif x % base == 0:
            b += "0"
            x -= 0
    return b[::-1]
    

