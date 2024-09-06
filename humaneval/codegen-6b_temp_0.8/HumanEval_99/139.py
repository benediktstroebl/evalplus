
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
    def closest_int(value):
        if value[-1] == '.':
            integer = int(value[:-1])
        else:
            integer = int(value)
        int_list = [x for x in range(-integer, integer+1)]
        int_list = sorted(int_list, key=lambda x: abs(x-int(value)))
        if int_list[0] == int(value):
            return int_list[0]
        elif int_list[1] == int(value):
            return int_list[1]
        elif int_list[0] > 0 and int_list[1] < 0:
            return int_list[0]
        else:
            return int_list[1]

    return closest_int(value)

