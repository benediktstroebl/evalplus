

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
    elif base < 2:
        raise ValueError('base cannot be less than 2')
    else:
        # Use a list for the digits
        digits = []
        # Try until we get the remainder to zero
        while x > 0:
            rem = x % base
            # Append the digit to the left
            digits.insert(0, rem)
            # Calculate the next quotient
            x = x // base
        # Return the digits joined as a string
        return ''.join(str(digit) for digit in digits)

