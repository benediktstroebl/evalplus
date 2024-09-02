
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

    # 1) Take the value given as a string and convert it into a number
    # 2) Check the remainder of dividing the number by 1. If the remainder is
    # 0 then the number is an integer, return it.
    # 3) If the remainder is not 0 then do the following:
    # - check the quotient. If it's negative then the number is closer to the
    #   next integer down, otherwise it's closer to the next integer up.
    # - check the difference between the number and the next integer in the
    #   correct direction. If it's more than the next integer is away from 0
    #   then return that integer, otherwise return the original number rounded.

    number = float(value)
    if number % 1 == 0:
        return int(number)
    quotient = abs(number) % 1
    if quotient > 0.5:
        if number < 0:
            return int(number - 1)
        else:
            return int(number + 1)
    elif number < 0:
        return int(number + 0.5)
    else:
        return int(number - 0.5)

