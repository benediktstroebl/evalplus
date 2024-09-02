

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
    if x<0:
        x=abs(x)
        negative=True
    else:
        negative=False

    if (base>10 and base<28):
        if x<10:
            changed_num=str(x)
        else:
            changed_num=change_base(int(str(x)[-1]), base)+change_base(int(str(x)[:-1]), base)
    elif (base>27 and base<36):
        if x<10:
            changed_num=str(x)
        else:
            changed_num=change_base(int(str(x)[-1]), base)+change_base(int(str(x)[:-1]), base)
    else:
        print("base number is out of range")
        return "ERROR"

    if negative:
        return "-"+changed_num
    else:
        return changed_num

