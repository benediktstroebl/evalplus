
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

    int_list = [int(x) for x in str(value)]

    if len(int_list) == 1:
        return int(int_list[0])

    diff_1 = abs(int_list[0]-int_list[1])
    diff_2 = abs(int_list[0]-int_list[-1])

    if diff_2 < diff_1:
        return int(int_list[0])
    elif diff_1 < diff_2:
        return int(int_list[-1])
    else:
        if int_list[0] > int_list[-1]:
            return int(int_list[0])
        else:
            return int(int_list[-1])


