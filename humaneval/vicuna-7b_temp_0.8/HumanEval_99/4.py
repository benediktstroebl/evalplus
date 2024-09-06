
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
    # To check if the number is equidistant from two integers, we check
    # if it is less than or greater than the two integers. If that's the case,
    # we round away from zero.
    if value in (int(value) - 1, int(value) + 1):
        # The number is equidistant from two integers, so round away from zero
        return int(round(value, 0))
    else:
        # The number is not equidistant from two integers, so return it as is
        return int(value)
