
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
    if value.isdigit() and value.isalpha() == False:
        return int(value)
    else:
        num_str = str(round(float(value),2))
        closest_int = int(num_str)
        for int_str in [str(i) for i in range(10) if i == closest_int]:
            if int_str != num_str:
                return int(num_str)
        else:
            return int(num_str)
