
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

    value = float(value)
    if value == int(value):
        return value
    else:
        sign = value.is_integer()
        if sign:
            return int(value)
        else:
            return round(value) if value > 0 else -round(value)

    # or
    return (sign, int(value) if value > 0 else -int(value))[int(abs(value) - abs(int(value))) == 0]
