
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

    value = int(value)

    nearest_integer = value
    if abs(value) - value > 0:
        diff_from_zero = abs(math.floor(value) - value)
        nearest_integer = math.floor(value)

    elif abs(value) - value < 0:

        diff_from_zero = abs(math.ceil(value) - value)
        nearest_integer = math.ceil(value)

    return abs(nearest_integer)

