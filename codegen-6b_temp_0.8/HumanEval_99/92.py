
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
    # convert the given value into a float
    value = float(value)

    # check if the value is positive or negative
    # if the value is positive, round it down to the nearest integer
    # if the value is negative, round it up to the nearest integer
    if value >= 0:
        return int(math.floor(value))
    else:
        return int(math.ceil(value))
