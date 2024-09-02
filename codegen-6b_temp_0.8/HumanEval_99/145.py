
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
    if "." not in value:
        return int(value)

    digit_list = [int(c) for c in value]

    if digit_list[0] == 0:
        digit_list = digit_list[1:]

    if len(digit_list) == 1:
        return int(digit_list[0])

    floating_point = value[:value.find(".")]
    integer = value[value.find(".") + 1:]

    integer_list = [int(c) for c in integer]

    if integer_list[0] == 0:
        integer_list = integer_list[1:]

    if len(integer_list) == 1:
        return int(integer_list[0])

    floating_point_list = [float(c) for c in floating_point]

    closest = 0
    key = 0
    for i, v in enumerate(floating_point_list):
        if abs(closest) > abs(v):
            closest = v
            key = i

    if closest == 0:
        return int(integer_list[-1])
    else:
        return int(integer_list[key])

