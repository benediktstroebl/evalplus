
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    # return None if arr is empty
    if len(arr) == 0:
        return None

    # set the accumulator to be the first element of the array
    accumulator = arr[0]
    for i in range(1, len(arr)):
        # determine if the number at the current index is positive or negative
        if arr[i] >= 0:
            # if the number is positive, then we know that it is either
            # 0 or 1, and so we can multiply the accumulator by it
            accumulator *= arr[i]
        elif arr[i] < 0:
            # if the number is negative, then we know that it is either
            # 0, -1, or -2, and so we can add it to the accumulator
            accumulator += arr[i]
    return abs(accumulator)
