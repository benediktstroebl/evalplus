
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    # strip the decimal point
    value = value.split('.')[0]

    # split the value into integers
    a, b = int(value), int(value)

    # if we have one integer, return the integer
    if abs(a) == abs(b):
        return int(value)

    # otherwise, we need to find the greater integer
    if abs(a) < abs(b):
        return int(value) - 1
    else:
        return int(value) + 1
