

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
    def get_digits(x, tens=0, ones=0):
        if x == 0:
            return tens + ones
        else:
            return get_digits(x // tens, tens + ones, x % tens) + (ones,)

    tens = int(base) - 1
    while tens >= 0:
        ones = get_digits(x, tens + 1, 0)
        x, tens = get_digits(x, tens, 1)
        if tens == 0:
            break
    else:
        return "0" * (x // base) + str(x % base)
    return "".join(str(d) for d in ones)
