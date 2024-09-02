
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
    digit = -1
    closest = None
    n = int(value)

    if n in [0, n//2, n//2-1]:
        return n

    for i in [1, -1]:
        if (abs(n-i) == abs(n//2-i) or abs(n+i) == abs(n//2+i)):
            digit = abs(n-i)
        elif closest is None or abs(n-i) < digit:
            digit = abs(n-i)
            closest = n + i
        elif abs(n-i) == digit:
            closest = n + i
    return closest
