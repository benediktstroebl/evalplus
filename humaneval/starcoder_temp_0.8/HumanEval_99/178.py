
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

    if not isinstance(value, str):
        return None

    num = int(value)
    if num < 0:
        num = -num
    if num % 10!= 0:
        num = num - num % 10
    else:
        num = num - num % 10 + 10

    if value[0] == '-':
        return -num
    else:
        return num

