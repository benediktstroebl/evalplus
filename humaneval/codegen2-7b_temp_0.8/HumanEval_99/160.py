
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
    try:
        value = int(value)
    except ValueError:
        value = float(value)
    values = sorted(set(map(int, str(value).split('.'))))
    if len(values) == 2:
        return int(values[1])
    elif len(values) == 1:
        return values[0]
    else:
        return values[0] + 1 if abs(values[0] - value) < abs(values[1] - value) else values[1
