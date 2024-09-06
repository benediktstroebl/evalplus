

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
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert x >= 0, 'x is negative: {}'.format(x)

    # Convert digits in the input x to list of digits
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base

    # Build the converted number in reverse order
    digits.reverse()

    # Convert each digit to a corresponding character
    # then join the characters into a string
    chars = []
    for digit in digits:
        if digit >= 10:
            char = chr(ord('a') + digit - 10)
        else:
            char = str(digit)
        chars.append(char)
    return ''.join(chars)
