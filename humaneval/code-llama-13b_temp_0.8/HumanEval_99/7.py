
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
    # 1. Check if the number is already an integer
    if type(value) == int:
        return value
    # 2. If not, convert to float
    value = float(value)
    # 3. Check the decimal
    decimal = value % 1
    # 4. If decimal is 0 or equals to 0.5, then return the int
    if decimal == 0 or decimal == 0.5:
        return int(value)
    # 5. Check if the decimal is closer to 0 or 1
    if decimal < 0.5:
        return int(value)
    return int(value) + 1

