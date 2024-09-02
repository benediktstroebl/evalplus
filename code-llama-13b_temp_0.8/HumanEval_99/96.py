
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
    if float(value).is_integer():
        return float(value)

    int_value = float(value)
    int_value_to_round = int(int_value)
    abs_value = abs(int_value)
    if int_value < 0:
        abs_value = -abs_value
    if int_value - int_value_to_round > 0.5:
        if abs_value - int_value_to_round > 0.5:
            return -abs_value
        else:
            return -int_value_to_round
    else:
        if abs_value - int_value_to_round > 0.5:
            return abs_value
        else:
            return int_value_to_round

