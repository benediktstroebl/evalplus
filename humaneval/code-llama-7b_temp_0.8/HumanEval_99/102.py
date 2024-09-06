
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
    # int(value)
    value_int = int(value)
    value_str = str(value)
    if "." in value_str:
        value_int_check = value_str.split(".")
        if int(value_int_check[1]) > 0:
            if int(value_int_check[1]) / 2 >= 0.5:
                value_int = value_int + 1
            elif int(value_int_check[1]) / 2 < 0.5:
                value_int = value_int - 1
        elif int(value_int_check[1]) < 0:
            if int(value_int_check[1]) / 2 < 0.5:
                value_int = value_int - 1
            elif int(value_int_check[1]) / 2 >= 0.5:
                value_int = value_int + 1
    return value_int
