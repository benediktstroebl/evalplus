
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
    value = int(value)

    if int(value) == value:
        return value

    # 'round' is a built-in function that returns the rounded value of 'value'
    # It accepts two arguments:
    # 1. The number to round to
    # 2. An optional argument, which by default is 0. It accepts any value
    #   representing the power to which to round.
    #
    # It can also be used as a method on numbers, because rounding is
    # an operation that happens to numbers. For example, 2.5 rounded to 3
    # is rounded to 4, not to 2.
    #
    # To illustrate, here's a quick example:
    # >>> round(3.14, 2)
    # 3.14

    # The last argument (place to round to) can be negative,
    # but the floating point converters will round towards zero.
    # So the following will round toward zero, both in the above example:
    # >>> round(3.14, -2)
    # 3.0

    # To round a negative value towards zero, use the neg argument.
    # For example, round(-3.14, -2) will round 3.99999999999999 to -3

    # The floating point converters will round to the nearest even number
    # For exemple, round(0.5) will round to 1, when we expect to get 0
    # To round towards zero, use the even argument.
    # For example, round(-0.5, even=True) will round -1 to -1
    return round(value, -1 if value < 0 else 0)
