
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
    number = float(value)
    if number == 0:
        return 0
    number_int = int(number)
    if abs(number - number_int) < abs(number - number_int + 1):
        return number_int
    elif abs(number - number_int) < abs(number - number_int - 1):
        return number_int - 1
    else:
        return number_int + 1
