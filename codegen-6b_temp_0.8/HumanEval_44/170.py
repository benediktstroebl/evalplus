

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
    # convert the integer to string
    y = str(x)

    # reverse the string
    y = y[::-1]

    # get the length of the string
    l = len(y)

    # return the reverse of the string if length of the string is less than base
    if l < base:
        return y

    # number of zeros to add for the final output
    num_zeros = base - l

    # add the required zeros to the end of the string
    y = '0' * num_zeros + y

    # return the modified string
    return y
