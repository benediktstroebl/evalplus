
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
    if '.' in value:
        int_part = value.split('.')[0]
    else:
        int_part = value
    if int_part.startswith('-'):
        sign = -1.
        int_part = int_part[1:]
    else:
        sign = 1.
    int_part = float(int_part)
    if int_part == round(int_part):
        return int(int_part*sign)
    else:
        return int(round(int_part*sign))
