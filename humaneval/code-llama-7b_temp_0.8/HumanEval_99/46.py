
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
    # My Code
    if abs(float(value)-float(value//1)) == 0.5:
        return value//1+1
    else:
        return value//1

    # Instructor code
    # if value%1 >= 0.5:
    #     return value//1+1
    # else:
    #     return value//1

    # for i in range(0, abs(int(value))+1):
    #     if int(value) - i != 0:
    #         if (float(value) - int(value)) % i == 0:
    #             return int(value) - i

    # return 0
