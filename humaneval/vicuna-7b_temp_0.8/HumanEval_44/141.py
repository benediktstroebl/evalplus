

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
    # Check if base is less than 10
    if base < 10:
        # Check if base is a digit in the number
        if base in str(x):
            # If base is a digit, return the string representation with base
            return str(x)[:x//base] + str(x%base)
        else:
            # If base is not a digit, return the original number
            return x
    else:
        # If base is greater than 10, return the original number
        return x
