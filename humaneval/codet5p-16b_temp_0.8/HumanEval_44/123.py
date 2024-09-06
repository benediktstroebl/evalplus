

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

    if base > 10:
        print("base is bigger than 10")
    else:
        if x == 0:
            return "0"
        elif x == 1:
            return "1"
        else:
            if base > 10:
                print("base is bigger than 10")
            else:
                q = []
                while x > 0:
                    q.append(chr(x % base + 48))
                    x //= base
                return "".join(q[::-1])
