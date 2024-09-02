
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

    # check if value is a number
    if not value.isdigit():
        return None

    # convert value to a float
    float_value = float(value)

    # check if value is already an integer
    if float_value == int(float_value):
        return int(float_value)

    # calculate the closest integer
    closest_int = int(float_value)

    # calculate the absolute difference between the value and the closest integer
    abs_diff = abs(float_value - closest_int)

    # if the absolute difference is less than 0.5, round away from zero
    if abs_diff < 0.5:
        if float_value > 0:
            closest_int += 1
        else:
            closest_int -= 1

    return closest_int
