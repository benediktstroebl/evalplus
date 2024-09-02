
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
    # 1. Remove trailing zeros and leading 0's
    value = value.rstrip('0')
    # 2. If the value is less than 0.1 or greater than 10, return it as is
    if abs(float(value)) <= 0.1 or abs(float(value)) >= 10:
        return int(value)
    # 3. If the value is 0.1 or 0.9, round it away from zero
    elif float(value) == 0.1 or float(value) == 0.9:
        return int(round(float(value)))
    # 4. Otherwise, round it away from zero as usual
    else:
        return int(round(float(value)))
