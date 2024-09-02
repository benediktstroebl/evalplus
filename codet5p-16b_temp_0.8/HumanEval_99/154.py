
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
    if value.count(".") == 0:
        if int(value) == float(value):
            return int(value)
        else:
            return int(value) + 1
    elif value.count(".") == 1:
        if value.index(".") == len(value) - 1:
            return math.floor(float(value))
        else:
            integer = value.index(".")
            return math.ceil(float(value))
    else:
        return "Can't handle floats"
