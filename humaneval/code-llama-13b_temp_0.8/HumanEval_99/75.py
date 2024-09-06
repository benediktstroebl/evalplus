
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
    # Step 1: Convert the given string to a float.
    value = float(value)

    # Step 2: Find the difference between the given value and the next
    # integer value after it. The next integer value after it is the given
    # value plus 1.
    diff_to_next_int = 1 - (value % 1)

    # Step 3: Find the difference between the given value and the previous
    # integer value before it. The previous integer value before it is the
    # given value minus 1.
    diff_to_prev_int = value % 1

    # Step 4: If both the diffs are equal, the given value is equidistant
    # from two integers. In this case, return the absolute value of the
    # given value (so it is away from zero)
    if diff_to_next_int == diff_to_prev_int:
        return round(value)

    # Step 5: If the diff between the previous integer and the given value
    # is smaller than the diff between the given value and the next integer,
    # return the previous integer.
    if diff_to_prev_int < diff_to_next_int:
        return int(value - 1)

    # Step 6: If none of the conditions above are met, the diff between
    # the given value and the next integer is smaller, so return that.
    return int(value)

