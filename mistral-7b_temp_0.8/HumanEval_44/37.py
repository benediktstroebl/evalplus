

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
    if x <= 0:
        return '0'

    string_representation = ''
    while x > 0:
        reminder = x % base
        if reminder < 10:
            string_representation = str(reminder) + string_representation
        else:
            string_representation = chr(reminder - 10 + 97) + string_representation
        x = x // base

    return string_representation

