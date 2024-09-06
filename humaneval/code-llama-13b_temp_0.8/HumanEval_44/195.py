

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
    number_mapping = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

    if x == 0:
        return '0'

    result = ''
    while x > 0:
        div = x // base
        mod = x % base
        result += number_mapping[mod]
        x = div

    return result[::-1]

