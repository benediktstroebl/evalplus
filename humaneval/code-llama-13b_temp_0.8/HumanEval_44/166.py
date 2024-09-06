

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
    # We first check if the base is a number smaller than 10.
    if base < 10:
        # We check whether the number is 0.
        if x == 0:
            return '0'
        # We initialise the result string.
        result = ''
        # We start with the remainder.
        remainder = x % base
        # If the remainder is not 0, we add it to the string.
        if remainder != 0:
            result += str(remainder)
        # We then divide x by base and we take the integer part of the result.
        # We do this as many times as necessary until x is 0.
        while x // base != 0:
            # We take the integer part.
            x //= base
            remainder = x % base
            # We add the remainder to the string.
            result = str(remainder) + result
        # We return the result.
        return result
    # If the base is greater than 10, we raise an exception.
    else:
        raise ValueError("The base should be a number smaller than 10.")

