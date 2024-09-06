
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
    float_val = float(value)
    nearest_int = round(float_val)
    closest_int = nearest_int

    # check if the number is equidistant between two integers
    if abs(nearest_int - int(nearest_int)) == abs(nearest_int - int(nearest_int) + 1):
        # round away from zero
        if nearest_int < int(nearest_int):
            closest_int = nearest_int - 1
        else:
            closest_int = nearest_int + 1

    return closest_int
