
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
    # 1. If the last digit of the given number is even, return the number as an integer.
    # 2. If the last digit of the given number isn't even, take away the decimal point and round up.

    # 1. if value[-1] in ('0', '2', '4', '6', '8'):
    #     return int(value)
    # 2. elif value[-1] in ('1', '3', '5', '7', '9'):
    #     return int(math.ceil(float(value)))

    return int(round(float(value)))



    # if int(value) % 2 == 0:
    #     return int(value)
    # else:
    #     return int(math.ceil(float(value)))


