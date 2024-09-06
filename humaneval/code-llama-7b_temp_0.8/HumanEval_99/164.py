
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
    # 0.05 5
    # 0.005 1
    # 0.001 0
    # 0.01 1
    # 0.1 1
    # 10.01 11
    # 10.05 11
    # 10.1 11
    # -0.05 0
    # -0.005 0
    # -0.01 0
    # -0.1 0
    # -10.01 0
    # -10.05 0
    # -10.1 0
    # 10.0 10
    # 10.5 11
    # -10.0 0
    # -10.5 -11

    # Split the value to get the value
    values = value.split('.')

    # Check if it is a positive or negative number
    # if negative value, return negative integer
    if value[0] == '-':
        return -1 * int(values[0])

    # else, round the number
    # get the last digit of the value
    # if digit is greater than 4, round up else round down
    if int(values[1]) >= 4:
        return int(values[0]) + 1
    else:
        return int(values[0])
