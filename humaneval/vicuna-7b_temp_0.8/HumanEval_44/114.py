

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
    # Convert number to base 10 and then to desired base.
    # If the number has leading zeroes, that's how it will be represented in the desired base.
    # Convert each digit to the desired base.
    # The remaining digits are the same as in the original base.
    # Combine the digits to get the final representation.
    return str(int(x) // (10 ** (len(str(base)) - 1))) + str(int(x) % (10 ** (len(str(base)) - 1)))
