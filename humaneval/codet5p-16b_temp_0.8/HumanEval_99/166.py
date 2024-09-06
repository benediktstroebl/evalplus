
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

    value = float(value)
    if value.is_integer():
        return int(value)
    int1 = int(value)
    int2 = int1 - 1
    diff1 = abs(value - int1)
    diff2 = abs(value - int2)
    if diff1 < diff2:
        return int1
    else:
        return int2
