
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
    # Code here

    # Clearly, "value" will be a string representing a number, so we'll
    # need to convert it to a float so we can round it. We can convert
    # a string to a float with float(value), so add that as the first
    # line in your code.

    # Then, we can round the value with round(float(value)), which will
    # give us the closest integer to the given number.

    # However, this isn't the solution yet! What if the number is equidistant
    # from two integers? How can we round it away from zero? We could
    # subtract 0.1 from it and add 0.9 to it, but that would only work
    # for numbers less than or equal to zero!

    # Instead, we can add 0.5 to the number and then use floor() (which
    # rounds down) to get the correct integer. If we round it down, it's
    # more likely to be away from zero!

    # So, to wrap it all up, add 0.5 to the value, convert it to a float,
    # then use floor() to round it down to the nearest integer, then
    # return it.

    # The floor() function is provided in the math module, so import it at
    # the top of your file.
    from math import floor
    return floor(float(value) + 0.5)

