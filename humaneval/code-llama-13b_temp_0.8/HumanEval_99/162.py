
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
    # Step 1.
    # check if the input is a string
    if not isinstance(value, str):
        return 'The input is not a string'
    # Step 2.
    # check if the input is a number
    try:
        value = float(value)
    except ValueError:
        return 'The input is not a number'
    # Step 3.
    # check if the input is an integer
    if value % 1 == 0:
        return int(value)
    # Step 4.
    # round the number
    result = int(value) if abs(value) > abs(value - 1) else int(value + 1)
    return result
