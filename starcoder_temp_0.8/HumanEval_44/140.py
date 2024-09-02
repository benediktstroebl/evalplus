

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
    # Handle non-integer inputs
    try:
        x = int(x)
    except ValueError:
        raise ValueError('Input is not a number')

    # Handle non-integer base
    try:
        base = int(base)
    except ValueError:
        raise ValueError('Base is not a number')

    # Handle invalid base (e.g. 2 or 1)
    if base < 2:
        raise ValueError('Base cannot be less than 2')

    # Handle invalid number to be converted (e.g. -1 or 9)
    if x < 0:
        raise ValueError('Number to be converted cannot be negative')

    # Handle input 0
    if x == 0:
        return '0'

    # Convert base of input to decimal
    num_as_decimal = 0
    for digit in str(x):
        try:
            digit = int(digit)
        except ValueError:
            raise ValueError('Number to be converted is not a number')
        num_as_decimal = num_as_decimal * base + digit

    # Convert decimal to target base
    result_in_str = ''
    while num_as_decimal!= 0:
        result_in_str = str(num_as_decimal % base) + result_in_str
        num_as_decimal = int(num_as_decimal / base)
    return result_in_str
