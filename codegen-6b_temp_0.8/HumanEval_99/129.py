
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
    integer = 0
    number = 0
    number_1 = abs(int(str(float(value)).split('.')[0]))
    number_2 = abs(int(str(float(value)).split('.')[1]))

    if (abs(number_1 - number_2) < abs(number - integer)):
        integer = number_1

    if (abs(number_1 - number_2) > abs(number - integer)):
        integer = number_2

    if (number_1 == number_2):
        number = 0

    if (number == 0):
        return (integer)
    else:
        return (number)


