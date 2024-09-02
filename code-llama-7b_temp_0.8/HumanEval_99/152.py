
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

    if not isinstance(value, str):
        raise TypeError(
            'closest_integer() takes in a string as an argument.')

    try:
        float(value)
    except ValueError:
        raise ValueError(
            'closest_integer() takes in a number as an argument.')

    int_value = int(float(value))
    if value == str(int_value):
        return int_value
    else:
        return int(round(float(value)))

