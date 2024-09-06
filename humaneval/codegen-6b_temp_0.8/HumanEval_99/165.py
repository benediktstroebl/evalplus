
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
    def helper(num):
        '''
        Return the integer number that is closest to the given number.
        '''
        if num < 0:
            num = -num
        else:
            num = abs(num)
        if num <= 1:
            return num

        if round(num) == num:
            return int(num)
        else:
            if num == int(num):
                return num
            else:
                if num < int(num):
                    return round(num)
                else:
                    return int(round(num))
    return helper(float(value))

