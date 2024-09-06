

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
    print(str(x))
    # base number is less than 10
    if base < 10:
        # if the base number is 0
        if base == 0:
            return str(x)
        else:
            return str(x) + change_base(x, base - 1)
    else:
        # if the base number is 10
        if x < 10:
            return str(x)
        # if the base number is 11
        else:
            output = ""
            # loop until x reaches 0
            while x >= 10:
                # adding the last digit of x to the output
                output += str(x % base)
                # change the x to the remainder of x divided by the base
                x = x // base
            # adding the last digit of x to the output
            output += str(x)
            # change the output to the reversed version of output
            output = output[::-1]
            # return the output
            return output
