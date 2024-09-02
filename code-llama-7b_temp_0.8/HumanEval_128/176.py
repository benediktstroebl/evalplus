
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
    if len(arr) == 1:
        return arr[0]

    # array of signs
    signs = [0] * len(arr)
    # product of signs
    prod = 1

    for i in range(len(arr)):
        # if current number is 0, then all numbers multiplied by 0 = 0
        if arr[i] == 0:
            return 0
        else:
            # if number is negative, it's sign will be -1
            if arr[i] < 0:
                signs[i] = -1
            else:
                signs[i] = 1
            # product of current signs of numbers in array
            prod *= signs[i]
            # update product of all numbers multiplied by their sign
            arr[i] = signs[i] * abs(arr[i])

    return sum(arr) * prod

