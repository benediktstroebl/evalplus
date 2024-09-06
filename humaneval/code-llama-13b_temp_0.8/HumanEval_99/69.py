
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
    # return int(round(float(value))) # you can't handle the case of equidistance
    # return math.ceil(float(value)) if float(value) > 0 else math.floor(float(value))
    # return int(float(value))
    # return int(float(value) + .5)
    # return int(0.5 - math.copysign(0.5, value - int(value)))
    return int(round(value)) if abs(float(value) - round(value)) > 0.5 else round(value)
