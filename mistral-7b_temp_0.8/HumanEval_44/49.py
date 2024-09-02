

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
    num_str = str(x)
    digit_length = len(num_str)
    result = ""

    for i in range(digit_length):
        result += str(int(num_str[i]) % base)

    result = int(result) + base

    return result

