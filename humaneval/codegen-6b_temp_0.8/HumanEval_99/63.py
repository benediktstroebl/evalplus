
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
    # first, I convert the input to a float:
    input_float = float(value)
    # now I need to find the closest integer:
    # we can use the floor function:
    closest_int = math.floor(input_float)
    # so we need to find the absolute value of the difference between the
    # number and the closest integer:
    abs_int_diff = abs(input_float - closest_int)
    # we can use the abs function to do that:
    abs_int_diff = abs(input_float - closest_int)
    # and now the closest integer to the input is:
    return closest_int if abs_int_diff < abs_int_diff else abs_int_diff
