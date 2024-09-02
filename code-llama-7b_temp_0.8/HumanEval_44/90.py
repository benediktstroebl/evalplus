

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
    # Separate x into digits using division and modulus operator
    digits = []
    while x:
        digits.append(x % base)
        x //= base
    # Convert each digit into corresponding characters
    for i in range(len(digits)):
        digits[i] = str(digits[i]) if digits[i] != 10 else 'A'
    # return the list of characters in reverse order
    return ''.join(reversed(digits)) if digits else '0'

