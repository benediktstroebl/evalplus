
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

    # 1. Check if the value has a decimal point.
    # 2. If the value has a decimal point, round it.
    # 3. If the value does not have a decimal point, return the given value.
    # 4. Return the final answer.

    if '.' in value:
        return round(float(value))
    return int(value)

