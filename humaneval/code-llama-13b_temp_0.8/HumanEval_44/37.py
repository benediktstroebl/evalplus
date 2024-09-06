

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
    """
    We can convert a number to a string in base 10 using the str() function.
    We can convert a number to a different base using the int() function.
    The int function takes two arguments: a number and a base.
    """
    if not isinstance(base, int):
        raise TypeError('Base must be an integer.')

    # Converting to a decimal number.
    num = str(x)
    # We are storing the result in a list, because strings are immutable.
    result = list()
    while num:
        # get the remainder of the division and append it to the result
        result.append(int(num) % base)
        # Removing the remainder from the number.
        num = str(int(num) // base)

    return ''.join([str(i) for i in reversed(result)])
