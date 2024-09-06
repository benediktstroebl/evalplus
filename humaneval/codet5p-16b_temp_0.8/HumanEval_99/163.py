
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
    sign = -1 if value[0] == '-' else 1

    value = value.replace(".", "")
    if value == '0': return 0
    if '.' in value:
        numbers = list(map(int, value.split('.')))
        for i, n in enumerate(numbers[1:]):
            if n!= 0:
                value = ''.join(map(str, numbers[:i+1]))
                break
    else:
        value = int(value)
    value = sign * int(round(math.fabs(value)))

    return value

