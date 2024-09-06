
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
    negative = False
    if value[0] == "-":
        negative = True
        value = value[1:]
    if '.' in value:
        value = value.split('.')[0]
    try:
        value = int(value)
    except ValueError:
        return None
    
    if abs(value) - int(abs(value)) < 0.5:
        if negative:
            return -int(abs(value))
        return int(abs(value))
    if value < 0:
        return -1 * (int(abs(value)) + 1)
    return int(abs(value)) + 1
