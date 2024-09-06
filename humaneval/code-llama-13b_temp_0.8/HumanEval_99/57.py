
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
    # Checks if value is a string
    if not isinstance(value, str):
        # Raises an error if not a string
        raise TypeError('You should input a string')
    # If value is a string
    else:
        # Checks if value is numeric
        try:
            # Converts to float
            number = float(value)
        except ValueError:
            # Raises error if not numeric
            raise ValueError('You should input a numeric value')
        # If value is numeric
        else:
            # Checks if value is positive
            if number >= 0:
                # If value is positive, rounds up
                if number % 1 >= 0.5:
                    return int(number + 1)
                # If value is positive, rounds down
                else:
                    return int(number)
            # If value is negative
            else:
                # If value is negative, rounds down
                if number % 1 <= -0.5:
                    return int(number - 1)
                # If value is negative, rounds up
                else:
                    return int(number)

