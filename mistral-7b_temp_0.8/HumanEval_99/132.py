
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
    # this function will return closest integer
    # to the inputed string

    # need to change the inputed string into float
    input_num = float(value)

    # use rounding function to round up or down the inputed string
    # based on the number given
    rounded_num = round(input_num)

    # return the rounded_num
    return rounded_num

