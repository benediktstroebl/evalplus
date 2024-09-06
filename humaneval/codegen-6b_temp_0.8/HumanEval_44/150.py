

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
    def convert_to_str(num: int, base: int):
        """convert an integer number to string, using recursion.
        base number is less than 10.
        >>> convert_to_str(8, 3)
        '22'
        >>> convert_to_str(8, 2)
        '1000'
        >>> convert_to_str(7, 2)
        '111'
        """
        converted_num = ""
        while num >= base:
            converted_num = str(num % base) + converted_num
            num //= base
        converted_num = str(num) + converted_num
        return converted_num

    if base > 10:
        raise ValueError("base cannot be greater than 10")
    elif x < 0:
        raise ValueError("number cannot be negative")
    elif base == 10:
        return str(x)
    else:
        converted_num = convert_to_str(abs(x), base)
        if x < 0:
            converted_num = "-" + converted_num
        return converted_num

