
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

    import math

    if value.isdigit():
        if float(value) % 1 == 0:
            value = int(value)
            return value
        else:
            value = float(value)
            if value < 0:
                value = value * -1
            result = round(value)
            return int(result)
    else:
        num = int(value[0:value.find('.')])
        if value.find('.')!= -1:
            point = float('0.' + value[value.find('.')+1:])
        else:
            point = 0
        value = math.ceil(num + point)
        return value


