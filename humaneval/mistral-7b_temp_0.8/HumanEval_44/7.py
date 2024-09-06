

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

    base = int(base)
    x = int(x)

    # Sanity check
    if base < 10:
        # convert to base 10
        x = str(bin(x))
        x = x[2:]
        # convert to base 10
        x = int(x)

        # convert to given base
        l = []
        while x > 0:
            x, r = divmod(x, base)
            l.append(str(r))
        l = l[::-1]
        s = ''.join(l)
        return s

    else:
        raise Exception('number should be less than 10')



























































































