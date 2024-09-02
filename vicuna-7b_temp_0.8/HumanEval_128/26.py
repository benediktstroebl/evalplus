
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
    if not arr:
        return None

    # initialize the result
    result = 0

    for i in range(len(arr)):
        # initialize the sign
        sign = 1

        for j in range(i, len(arr)):
            # if the current number is greater than the previous one, the sign is -1
            if arr[j] > arr[i]:
                sign = -1
            # if the current number is less than the previous one, the sign is 1
            elif arr[j] < arr[i]:
                sign = 1
            # if the current number is equal to the previous one, the sign is 0
            else:
                sign = 0

            # multiply the magnitude and the sign
            result *= arr[i] * sign

    return result
