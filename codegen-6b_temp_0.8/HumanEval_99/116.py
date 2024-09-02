
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
    # Get the two closest integers
    num1 = closest_integer_helper(value)
    num2 = closest_integer_helper(value, num1)

    # If the two integers are the same, round the result away from zero
    if num1 == num2:
        return num1 if num1 >= 0 else num2

    # Otherwise, return the result of the larger integer (closest to zero)
    return num1 if num1 >= num2 else num2

