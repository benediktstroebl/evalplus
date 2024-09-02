

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
    new_num = []
    x_str = str(x)
    max_digit = len(x_str) - 1
    for index, digit in enumerate(x_str):
        if int(digit) >= base:
            max_digit = index
            break
    for i in range(max_digit, -1, -1):
        digit = int(x_str[i])
        as_digit = digit + base - 10 * i
        if as_digit >= base:
            new_num.append(chr(as_digit + ord('A') - 10 * i))
        else:
            new_num.append(str(as_digit))
    return ''.join(new_num[::-1])
    
        