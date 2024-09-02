
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # check for zero, one or two elements
    if len(arr) <= 2:
        return -1

    # find the largest and the smallest values in the array
    max_val, min_val = max(arr), min(arr)

    # initialise the result to be the smallest value in the array
    result = min_val

    # check if the min value is 1 and if the max value is greater than two
    if min_val == 1 and max_val > 2:
        # if the largest value in the array is greater than two then we know
        # that a valid solution does not exist
        if max_val % 2 != 0:
            return -1
        # otherwise divide the largest value in the array by two and update
        # result to be this value
        else:
            result = max_val // 2

    # for the rest of the values in the array...
    for val in arr:
        # if the current value is greater than or equal to the result then it
        # can not be arranged
        if val >= result:
            return -1

        # otherwise increment the result by 1
        result += 1

        # if the result is greater than the max value then we know that a valid
        # solution does not exist
        if result > max_val:
            return -1

    return result
