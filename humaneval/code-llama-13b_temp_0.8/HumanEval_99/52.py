
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

    import math
    # first, we convert the string into float
    float_number = float(value)

    # we check if float is integer or not
    if float_number.is_integer():
        return int(float_number)

    # if float is not an integer, we find the closest integers
    else:
        # We find the closest integer that is lower than float
        lower = math.floor(float_number)

        # We find the closest integer that is greater than float
        upper = math.ceil(float_number)

        # we create a list with those two integers
        integer_list = [lower, upper]

        # we find the absolute values of those integers
        abs_lower = abs(lower)
        abs_upper = abs(upper)

        # we create a list with those absolute values
        abs_integer_list = [abs_lower, abs_upper]

        # we find the minimum of those integers
        min_abs_integer = min(abs_integer_list)

        # we find the index of the minimum in the original list
        # we can use that index to find the closest integer
        index_min_abs_integer = abs_integer_list.index(min_abs_integer)
        closest_integer = integer_list[index_min_abs_integer]

        return closest_integer

