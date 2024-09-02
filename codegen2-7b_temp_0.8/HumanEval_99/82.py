
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
    if type(value)!= str:
        raise TypeError("Argument must be a string")
    try:
        value = float(value)
    except:
        raise ValueError("Argument must be a number")
    if value.is_integer():
        return int(value)
    else:
        value = abs(value)
        number_list = [number for number in range(int(value))]
        number_list.sort()
        return number_list[int((len(number_list) - 1) / 2)]

