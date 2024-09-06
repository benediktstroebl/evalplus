
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

    int_value = int(value)
    int_floor = math.floor(int_value)
    int_ceil = math.ceil(int_value)

    if int_value < 0:
        int_floor = -int_floor
        int_ceil = -int_ceil

    if int_value == math.floor(int_value):
        return int_floor

    if int_value == math.ceil(int_value):
        return int_ceil

    return int_floor if abs(math.floor(int_value)) < abs(math.ceil(int_value)) else int_ceil

