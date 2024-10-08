
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
    def closest_integer_helper(number, closest, bigger):
        if number == closest:
            return closest
        elif number > closest and number < closest + bigger:
            return closest + bigger
        elif number < closest and number > closest - bigger:
            return closest - bigger
        else:
            return closest + bigger if number > closest else closest - bigger

    return float(closest_integer_helper(float(value), 0, 1))
