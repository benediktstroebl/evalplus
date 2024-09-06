
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
    int_number = float(value)
    rounded_number = int(round(int_number))
    if abs(rounded_number - int_number) < abs(int_number - int(math.floor(int_number))):
        return math.ceil(int_number)
    else:
        return math.floor(int_number)
