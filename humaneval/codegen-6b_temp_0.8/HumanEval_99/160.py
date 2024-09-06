
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
    value_int = int(value)
    closest = int(value)
    if value_int < 0:
        closest = -closest
    else:
        closest = closest
    is_divisble_by_three = closest / 3
    if is_divisble_by_three == 0:
        is_divisble_by_three = closest // 3

    if is_divisble_by_three * 3 == closest:
        closest = is_divisble_by_three
    else:
        closest = closest - is_divisble_by_three * 3

    if value_int < 0 and closest > -1 * closest:
        closest = -1 * closest
    elif value_int > 0 and closest > closest:
        closest = closest

    return closest

