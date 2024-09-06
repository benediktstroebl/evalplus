
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
    if value is not None:
        if isinstance(value, int):
            return value
        try:
            val = float(value)
        except ValueError:
            return int(value)
        else:
            if val - int(val) == 0:
                return int(val)
            else:
                return int(val + 0.5)
    else:
        return None

