
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

    integer = int(value)
    int1 = integer-1
    int2 = integer+1
    diff1 = abs(int1 - integer)
    diff2 = abs(int2 - integer)
    if diff2 < diff1:
        return int2
    else:
        return int1
