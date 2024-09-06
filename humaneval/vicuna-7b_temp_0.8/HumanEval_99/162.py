
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
    # Use the decimal.Decimal function to convert the float to a decimal
    # value, which allows for better accuracy when comparing to integers
    decimal = decimal.Decimal(value)

    # Check if the number is already an integer
    if decimal.is_integer() == True:
        return int(decimal)

    # Otherwise, check if the number is within range of 1 integer
    if abs(decimal - int(decimal)) < 1:
        return int(decimal)

    # If not, check which integer is closest to the number
    nearest_integer = int(decimal)
    farthest_integer = int(decimal - 1)

    # Check if the number is exactly halfway between two integers
    if abs(nearest_integer - farthest_integer) < 1:
        return round(farthest_integer - 1)

    # Otherwise, round away from zero
    return round(nearest_integer)
