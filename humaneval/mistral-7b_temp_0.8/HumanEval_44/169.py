

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
    # num = x
    # if x == 0:
    #     return "0"
    # ret = ""
    # while x > 0:
    #     ret = str(x % base) + ret
    #     x //= base
    # return ret
    # return list(map(str, list(map(int, str(x)))))

    if x == 0:
        return "0"
    ret = []
    while x > 0:
        x, mod = divmod(x, base)
        ret.append(str(mod))
    return "".join(ret[::-1])

