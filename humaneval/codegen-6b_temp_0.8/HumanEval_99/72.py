
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
    def function(string):
        s = string.split(".")
        n = s[0]
        n = int(n)
        m = s[1]
        m = int(m)
        if m < 5:
            return round(n)
        elif m > 5:
            return round(n) + 1
        return round(n)
    return function

