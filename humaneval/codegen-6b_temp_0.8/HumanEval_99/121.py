
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
    # convert the value entered to an int
    value = int(value)
    # define two integers, subtracting 14.5 from each will make the
    # two integers equidistant from 14.5, return the one that is farther
    # from zero
    int1 = value - 14.5
    int2 = value - 17.5
    if int1 < int2:
        return int1
    else:
        return int2
