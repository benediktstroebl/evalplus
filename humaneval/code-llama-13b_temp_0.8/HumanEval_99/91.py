
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

    # 1. Check if the value is an integer (string)
    # 2. If it is, return it as an integer
    # 3. If it isn't, convert it to a float (to make sure it isn't an integer)
    # 4. Check if it's positive or negative
    # 5. Round it
    # 6. If it's positive, convert it to an integer and return it
    # 7. If it's negative, convert it to an integer and return it

    # 1
    if value.isdigit():
        return int(value)

    # 3
    float_value = float(value)

    # 4
    if float_value >= 0:
        # 5
        round_value = round(float_value)

        # 6
        return int(round_value)
    else:
        # 5
        round_value = -round(-float_value)

        # 7
        return int(-round_value)
