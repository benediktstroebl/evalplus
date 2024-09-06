
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
    if type(value) is not str:
        raise TypeError("Invalid argument type. Expected string, got {0}.".format(type(value)))
    if not value.isnumeric():
        raise ValueError("Invalid argument value. Expected numeric string, got {0}.".format(value))
    # Your code here
    value = float(value)
    if value.is_integer():
        return value
    else:
        return round(value) if value >= 0 else -round(abs(value))

