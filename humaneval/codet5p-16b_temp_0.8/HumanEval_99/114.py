
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

    from math import copysign
    value = str(value)
    int_value = int(float(value))
    dif = abs(int_value - float(value))
    if int_value < 0:
        dif = abs(int_value - float(value))
    else:
        dif = abs(int_value - float(value))
    print(dif)
    if dif > 0.5:
        return int_value
    else:
        return int_value + copysign(0.5, int_value)
