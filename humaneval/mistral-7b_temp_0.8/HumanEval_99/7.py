
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
    closest_number = value

    # add your code here
    if len(value) == 0:
        return 0
    elif len(value) == 1:
        return int(value)
    else:
        if int(value[0]) > int(value[1]):
            closest_number = int(value[:1])
        else:
            closest_number = int(value[1:])

    return closest_number
