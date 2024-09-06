
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

    # 1. Split the string into the integer part and the decimal part.
    # 2. Add 0.5 to the decimal part.
    # 3. Convert it to an integer.
    # 4. Return the original number if the integer part is equal to it.
    # 5. Otherwise, return the integer part.

    integer, decimal = value.split('.')

    decimal = float('.' + decimal)
    decimal += 0.5

    decimal = int(decimal)

    if int(integer) == decimal:
        return int(integer)

    return decimal

