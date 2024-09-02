
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
    # split the value by '.'
    value_parts = value.split('.')
    # find the integer part
    int_part = value_parts[0]
    # convert the rest to an integer
    float_part = int(value_parts[1])
    # if the number is less than 1, it's an integer
    if int(value) < 1:
        return int_part
    # if the number is more than 1, we need to round
    else:
        if float_part > 0.5:
            return int_part + 1
        else:
            return int_part
