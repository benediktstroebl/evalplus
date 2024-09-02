
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

    # from math import ceil, floor
    #
    # is_negative = '-' in value
    #
    # value = abs(float(value))
    #
    # int_value = int(value)
    #
    # ceil_value = ceil(value)
    # floor_value = floor(value)
    #
    # if ceil_value - value == value - floor_value:
    #     if is_negative:
    #         return -floor_value
    #     else:
    #         return int_value
    #
    # elif ceil_value - value < value - floor_value:
    #     if is_negative:
    #         return -ceil_value
    #     else:
    #         return ceil_value
    #
    # else:
    #     if is_negative:
    #         return -floor_value
    #     else:
    #         return int_value

    return int(value) if abs(float(value)) - int(value) > 0.5 else int(value) + (1 if float(value) > 0 else -1)

