
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
    # You can use the following code snippet to convert string to float
    # value = float(value)
    # and then use the following code snippet to check if it is
    # equidistant from two integers
    # round_to_integer = 0
    # if abs(value - (round_to_integer + 0.5)) < abs(value - (round_to_integer - 0.5)):
    #     round_to_integer += 0.5
    # else:
    #     round_to_integer += 0.5
    # return round_to_integer

    # instead of this
    # round_to_integer = 0
    # if abs(value - round_to_integer) < abs(value - round_to_integer - 0.5):
    #     round_to_integer += 0.5
    # else:
    #     round_to_integer += 0.5
    # return round_to_integer

    # or this
    # round_to_integer = 0
    # if abs(value - round_to_integer) < abs(value - round_to_integer - 0.5):
    #     round_to_integer += 0.5
    # return round_to_integer

    # This is the most efficient way to do it
    return int(value)