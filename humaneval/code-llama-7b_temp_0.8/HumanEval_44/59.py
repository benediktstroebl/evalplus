

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
    if x == 0:
        return '0'
    # Determine the number of digits in input number:
    len_x = 1
    while x // (base ** len_x):
        len_x += 1
    result = ''
    # Perform the actual conversion:
    for i in range(len_x - 1, -1, -1):
        # Determine the rightmost digit:
        digit = x // (base ** i)
        x %= (base ** i)
        # Convert the digit to its corresponding character in the new base:
        result += str(digit)
    return result

