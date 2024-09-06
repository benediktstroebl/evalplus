

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
    # import a library that we will need
    import math

    # write our code here
    new_base_int = len(str(base))
    new_base_number = [math.floor(x / (base ** new_base_int)) % base]
    for i in range(new_base_int-1, -1, -1):
        new_base_number.append(math.floor(x / (base ** i)) % base)
    new_base_number.reverse()
    return ''.join(map(str, new_base_number))
