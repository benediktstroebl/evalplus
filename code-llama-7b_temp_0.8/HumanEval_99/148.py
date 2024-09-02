
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

    # try to convert it to a float, raise exception if it can't
    try:
        num = float(value)
    except:
        raise Exception("Value must be a number")

    # find the integer part of the float
    integer = int(num)

    # figure out the integer that is the closest to the number
    closest = integer
    if abs(num - integer) < abs(num - integer + 1):
        closest = integer + 1

    return closest
