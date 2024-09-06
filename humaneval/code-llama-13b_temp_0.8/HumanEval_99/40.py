
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
    # set to int
    value = float(value)

    # if less than zero, subtract one
    if value < 0:
        value -= 1

    # if greater than zero, add one
    elif value > 0:
        value += 1

    # if equal to zero, return zero
    else:
        return 0

    # cast as int
    return int(value)

