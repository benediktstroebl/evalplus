

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
    assert base > 1

    # you can use any code here

    if base < 10:
        return str(x)
    else:
        result = ""
        while x:
            if base == 2:
                result += str(x % 2)
            elif base == 3:
                result += str(x % 3)
            elif base == 8:
                result += str(x % 8)
            elif base == 16:
                result += str(x % 16)
            else:
                raise ValueError(f'Invalid base value')

            x = x // base

        return result[::-1]

