
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
    import math

    # split the number at decimal (if present)
    number_split = value.split('.')
    if len(number_split) > 1:
        # find the index of the first element
        index = value.index('.')
        # add 1 to the index to be able to access the element
        index += 1

        # create a dict of data structure {value : index}
        # to be able to send the decimal part back to the main func
        dd = {value[index:] : index}
        # create a dict to store the diff between
        # the two integers and the value
        diffs = {}

        for key, value in dd.items():
            two_numbers = key.split('.')
            # set the two integers as the first two elements
            first_one = int(two_numbers[0])
            second_one = int(two_numbers[1])

            # create a dict to store the diff between the two integers
            diff = {}
            diff[first_one] = second_one - first_one
            diff[second_one] = first_one - second_one
            diffs[value] = diff

        # get the dictionary value with the minimum diff
        # to round the number (in case it's equidistant from two integers)
        different_diffs = dict(
            filter(lambda x: x[1] != 0, diffs.items())
        )
        closest_diff = min(different_diffs, key=lambda x: abs(x))
        # return the rounded number (or the original given number)
        return int(round(float(value)))
    else:
        return int(value)

