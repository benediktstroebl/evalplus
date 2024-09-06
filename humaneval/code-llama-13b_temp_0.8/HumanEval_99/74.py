
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
    # Step 1: Convert the given number to a floating-point number
    # Step 2: Convert the resulting floating-point number to an integer
    # Step 3: If the absolute value of the difference between the given
    # floating-point number and resulting integer is less than or equal to
    # 0.5, return the resulting integer as the result
    # Step 4: Otherwise, if the given number is positive, return the
    # resulting integer incremented by 1
    # Step 5: If the given number is negative, return the resulting
    # integer decremented by 1
    pass
