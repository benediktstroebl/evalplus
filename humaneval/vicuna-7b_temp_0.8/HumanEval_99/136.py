
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
    n = int(value)
    while True:
        if value[-1] == '0':
            n += 1
            value = value[:-1]
        elif value[-1] == '.':
            i = n // 2
            while '0' in value[:i]:
                value = value[:i]
                n = n // 2
            if n % 2 == 0:
                break
        else:
            break
    return n
