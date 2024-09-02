
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
    # Your code here
    def closest_integer(value):
        str_value = str(value)
        int_part = int(str_value)
        if value < 0:
            if len(str_value) > 1:
                if int_part == 0:
                    return -1
                else:
                    return -1- int_part
            else:
                return -1
        elif value > 0:
            if len(str_value) > 1:
                if int_part == 0:
                    return 1
                else:
                    return 1 + int_part
            else:
                return 1
        else:
            return int_part
    return closest_integer(value)
