
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

    # The first line is just to check that you've passed in a string.
    # If not, the test will raise an error.
    if type(value) != str:
        raise TypeError('expected a string')

    # Convert string to float
    num = float(value)

    # If num is an integer, return it
    if num % 1 == 0:
        return num

    # If num is not an integer, return the round
    elif num > 0:
        return round(num)

    # If num is negative and > 0, return the floor
    else:
        return int(num)
