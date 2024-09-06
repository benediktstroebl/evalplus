
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

    # if it's an integer, return it
    if value % 1 == 0:
        return value
    else:
        # if the number is positive
        if value > 0:
            # round up
            if value % 1 >= 0.5:
                return int(value) + 1
            # round down
            else:
                return int(value)
        # if the number is negative
        else:
            # round up
            if value % 1 >= 0.5:
                return int(value)
            # round down
            else:
                return int(value) - 1

