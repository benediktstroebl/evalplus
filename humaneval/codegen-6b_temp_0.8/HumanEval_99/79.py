
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
    import math

    # Check if the number is an integer, an integer after a decimal
    # and if the number is a positive or negative number.
    if value[-1] == '0' and value[-2] in '0123456789':
        value = int(value)
    elif value[-1] == '.' and value[-2] in '0123456789':
        value = float(value)
    else:
        raise ValueError('{} is not a number'.format(value))

    # Check if the given number is positive or negative and get its
    # sign from it.
    sign = 1
    if value < 0:
        sign = -1
        value = abs(value)

    # Round the number to the smallest integer.
    # For reference:
    # http://stackoverflow.com/questions/591009/rounding-functions-in-python
    return sign * round(value // 1) * 1

