
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
    # My solution
    def is_neg(val):
        if val.startswith('-'):
            return True
        return False

    def dec_len(val):
        return len(val.split('.')[1])

    def dec_len_min(val):
        if val == 0:
            return 1
        return len(str(val)) - 1

    def dec_val(val):
        if val == '':
            return 0
        return int(val)

    if value == '0':
        return 0

    if is_neg(value):
        value = value.lstrip('-')

    if '.' in value:
        dec_vals = value.split('.')
        dec_vals[1] = dec_vals[1].rstrip('0')
        decimal = int(dec_vals[1]) / dec_len(value)
        val = int(dec_vals[0]) + decimal
    else:
        val = int(value)

    val1 = round(val)
    val2 = round(val + 0.5)
    val1_dist = abs(val - val1)
    val2_dist = abs(val - val2)

    if val1_dist == val2_dist:
        if val1_dist == 0:
            return int(value)
        if dec_len_min(val) % 2 != 0:
            if is_neg(value):
                return val1
            else:
                return val2
        else:
            if is_neg(value):
                return val2
            else:
                return val1
    else:
        return round(val)

