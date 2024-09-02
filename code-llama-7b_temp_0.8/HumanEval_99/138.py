
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
    # convert string to float
    value = float(value)

    # get absolute value
    abs_value = abs(value)

    # get integer part
    int_part = abs_value // 1

    # calculate the decimal part
    decimal_part = abs_value % 1

    # If decimal part is less than 0.5, we will round towards the nearest integer part.
    # otherwise, we will round towards the integer part one bigger
    if decimal_part < 0.5:
        return int_part
    else:
        if value < 0:
            return int_part - 1
        else:
            return int_part + 1

