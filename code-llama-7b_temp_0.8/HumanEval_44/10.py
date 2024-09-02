

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
    # Convert the input to a string
    x_str = str(x)
    # Check the length of the input string
    if len(x_str) > 2 or base > 10:
        # If the number is more than 10^2,
        # or the base is more than 10,
        # return -1
        return -1
    # Initialise a variable to hold the result
    result = ''
    while x_str:
        # If x_str is not empty,
        # start a loop to get the result
        # in the target base
        result += str(x_str[0])
        x_str = x_str[1:]
        x = int(result)
        x = x * base
        result = str(x)
    return result

