
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
    num = float(value)
    if num.is_integer():
        return int(num)
    else:
        half_num = num/2
        if (math.ceil(half_num)) == (math.floor(half_num)):
            return int(math.floor(half_num))
        else:
            return int(math.ceil(half_num))
