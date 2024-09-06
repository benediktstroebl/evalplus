
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
    if type(value) == int or type(value) == float:
        return int(round(value))

    if value[-1] == '.':
        value = float(value)
    else:
        value = int(value)

    if value < -100:
        return -100
    elif value > 100:
        return 100

    nums = [math.floor(value), math.ceil(value)]
    nums.sort()
    return nums[1]

