
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
    if value.isdigit():
        return int(value)
    else:
        a = value.split(".")
        i = int(a[0])
        if len(a) > 1:
            dec = int(a[1])
            dec = dec / 10 ** (len(a[1])-1)
            if i < 0:
                i = abs(i)
                dec *= -1
            c = i + dec
            if c % 1 >= 0.5:
                i = int(c) + 1
            else:
                i = int(c)
        return i
