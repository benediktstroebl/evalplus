
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

    # 1. if value is integer, return the value
    # 2. if value is float, round the number to the closest integer
    # 3. if value is negative float,
    # 4. round down to next integer
    # 5. if value is positive float, round up to next integer

    # 1
    if str(value).isdigit():
        return int(value)

    # 2
    value = round(float(value))

    # 3
    if value < 0:
        return value - 1
    else:
        # 4
        return value + 1

