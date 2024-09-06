
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
    if value.isdigit() and value.isnumeric() and value != '0':
        try:
            value = int(value)
            return value
        except ValueError:
            pass

        left = 1
        right = 9
        while True:
            mid = (left + right) // 2
            if mid == 5:
                return mid + 1
            elif mid % 2 == 0:
                return mid
            elif mid % 3 == 0:
                return mid
            elif mid % 2 == 1:
                return mid + 1
            else:
                right = mid - 1
        return 0

    else:
        return None
