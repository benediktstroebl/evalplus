
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

    # return int(value)
    # .5 or greater should round up
    # less than -.5 should round down

    if value.isdigit():
        return int(value)

    value = float(value)

    if value % 1 >= .5:
        return int(value + 1)

    if value % 1 < -.5:
        return int(value - 1)

    return int(value)

    # return value if value % 1 == 0 else int(value)

