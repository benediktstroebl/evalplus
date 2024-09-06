
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
    new_value = ""
    if "." in value:
        new_value = value[:value.index(".")]
        decimal = True
    else:
        new_value = value
        decimal = False

    if new_value.isdigit() == True:
        if decimal == True:
            return float(new_value)
        else:
            return int(new_value)
    else:
        array = new_value.split(".")
        new_value = str(int(float(array[0]))) + "." + str(int(float(array[1])))
        if decimal == True:
            return float(new_value)
        else:
            return int(new_value)


