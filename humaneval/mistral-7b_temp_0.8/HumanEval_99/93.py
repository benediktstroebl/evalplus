
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
    number = value.split('.')
    if len(number) == 1:
        number = number[0]
        return int(number)
    else:
        int_number = number[0]
        float_number = number[1]
        if int_number[-1] == '5':
            if float_number == '5':
                int_number = int_number[:-1] + '6'
            else:
                int_number = int_number[:-1] + '4'
        else:
            if float_number == '5':
                int_number = int_number + '5'
            else:
                int_number = int_number + '0'
        return int(int_number)
