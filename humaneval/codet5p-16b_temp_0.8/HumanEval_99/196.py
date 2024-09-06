
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

    from math import floor
    import math

    neg = value.startswith("-")
    if neg:
        value = value[1:]
    result = value.split(".")
    if len(result) > 1:
        integer, fraction = result
    else:
        integer = result[0]
        fraction = ""
    integer = int(integer)
    fraction = float("0." + fraction)
    if fraction == 0:
        return int(integer)
    distance = abs(fraction)
    closest_integer = integer
    for i in range(1, int(integer)):
        try:
            new_fraction = math.floor(fraction - i)
            new_distance = abs(new_fraction)
            if new_distance < distance:
                closest_integer = i
                distance = new_distance
            elif new_distance == distance:
                closest_integer = i
                distance = new_distance
        except:
            pass
    if neg:
        closest_integer *= -1
    return int(
