
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
    # This function uses the fact that the decimal value is closest to the integer value
    # if the number of digits to the right of the decimal point is odd.
    # This is because the leftmost digit is more important than the rightmost digit.
    # To see this, consider the number 10.1. The rightmost digit is 1, which is
    # important for determining the value of the number. On the other hand,
    # the leftmost digit is 1, which has no effect on the value of the number.
    # So, to find the closest integer, you should round the number down
    # if the number of digits to the right of the decimal point is odd,
    # and round the number up if the number of digits to the right of the decimal point
    # is even.
    return round(value, 0, 1)
