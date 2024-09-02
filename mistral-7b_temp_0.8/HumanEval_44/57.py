

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
    binary = bin(x)[2:]
    new_binary = '0b'
    while len(binary) % base != 0:
        new_binary += '0'
    for i in range(len(binary) - len(new_binary), len(binary), base):
        new_binary += str(int(binary[i:i + base]))
    return new_binary

