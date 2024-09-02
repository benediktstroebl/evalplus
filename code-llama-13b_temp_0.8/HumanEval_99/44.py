
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
    # Code here

    from math import floor, ceil

    value = float(value)
    ceil_value = ceil(value)
    floor_value = floor(value)

    ceil_value_diff = abs(ceil_value - value)
    floor_value_diff = abs(value - floor_value)

    if ceil_value_diff == floor_value_diff:
        if value > 0:
            return int(ceil_value)
        return int(floor_value)
    elif ceil_value_diff < floor_value_diff:
        return int(ceil_value)
    return int(floor_value)
