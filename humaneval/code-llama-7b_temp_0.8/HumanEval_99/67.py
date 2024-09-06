
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

    # Method 1
    # value = float(value)
    # closest = 0
    # for i in range(-100, 100):
    #     if abs(value-i) < abs(value-closest):
    #         closest = i
    # return closest

    # Method 2
    # value = float(value)
    # closest = 0
    # diff = 1000
    # for i in range(-100, 100):
    #     new_diff = abs(value-i)
    #     if new_diff < diff:
    #         closest = i
    #         diff = new_diff
    # return closest

    # Method 3
    # import math
    # value = float(value)
    # return round(value) if abs(value-round(value)) < 0.5 else round(value+math.copysign(0.5, value))

    # Method 4
    # import math
    # value = float(value)
    # return round(value) if abs(value-round(value)) < 0.5 else round(value+math.copysign(0.5, value-round(value)))

    # Method 5
    # value = float(value)
    # return round(value) if abs(value-round(value)) < 0.5 else round(value+math.copysign(0.5, value-round(value)))

    # Method 6
    # value = float(value)
    # return int(value+0.5)

    # Method 7
    # value = float(value)
    # return int(value+0.5) if value>=0 else int(value-0.5)

    # Method 8
    # value = float(value)
    # return int(value+0.5) if value>0 else int(value-0.5)

    # Method 9
    # value = float(value)
    # return round(value) if abs(value-round(value)) < 0.5 else round(value+0.5) if value>=0 else round
