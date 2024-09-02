
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
    # Algorithm
    # If the given number is equidistant from two integers, round it away from zero.
    # Then we need to make a float number to integer type:
    # - If the given value is greater than the integer type:
    #   - If the fractional part of the given number is .5 or greater
    #     return the next integer type.
    #   - Otherwise return the previous integer type.
    # - If the given value is lower than the integer type:
    #   - If the fractional part of the given number is .5 or less
    #     return the previous integer type.
    #   - Otherwise return the next integer type.
    if value.find('.') != -1:
        fractional, integer = value.split('.')
        if int(fractional) == 0:
            return int(value)
        else:
            if int(fractional) < 5:
                return int(value) - 1
            else:
                return int(value)
    else:
        return int(value)
