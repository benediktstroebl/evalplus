
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
        return closest_integer(float(value))
    if value == int(value):
        return value
    nearest_int = 0
    for i in range(1, int(value) + 1):
        if value - i >= 0.5:
            if abs(value - i) < abs(value - (i + 1)):
                nearest_int = i
                break
        elif abs(value - (i + 1)) < abs(value - i):
            nearest_int = (i + 1)
            break
    return nearest_int
