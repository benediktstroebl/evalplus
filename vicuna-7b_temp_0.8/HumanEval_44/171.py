

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
    x_str = str(x)
    converted_str = ""
    for i in range(len(x_str)):
        if x_str[i] >= base:
            #convert the rest of the string
            converted_str += x_str[i]
            for j in range(i, len(x_str)):
                converted_str += "0"
            converted_str = converted_str.rjust(len(x_str), '0')
            #convert the last digit
            converted_str += str(x_str[i] // base)
            x_str = x_str[:i] + str(x_str[i]) + x_str[i+1:]
            break
    return converted_str