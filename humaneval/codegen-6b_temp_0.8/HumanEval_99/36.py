
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
    def closest_integer_helper(value):
        digits = [int(x) for x in value]
        max_digit = max(digits)
        min_digit = min(digits)
        diff = abs(max_digit - min_digit)

        if diff == 0:
            return max_digit

        if diff == 1:
            return digits[-1]

        return max_digit if max_digit >= 0 else min_digit

    return closest_integer_helper(value)

