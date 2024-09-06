

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
    assert 2 <= base < 10, 'Base must be between 2 and 10'

    base_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    result = ''
    while x != 0:
        quotient = x // base
        remainder = x % base
        result = base_dict[remainder] + result
        x = quotient
    return result

