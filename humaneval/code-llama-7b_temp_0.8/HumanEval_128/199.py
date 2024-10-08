
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

    # My and best solution
    if len(arr) == 0:
        return None
    arr2 = arr.copy()
    for i in range(len(arr)):
        if arr[i] < 0:
            arr2[i] *= -1

    return sum(arr) * (-1 if sum(arr2) < 0 else 1) * arr[0]


    # Best way
    # if len(arr) == 0:
    #     return None

    # product = 1
    # for i in arr:
    #     product *= (-1) if i < 0 else 1
    # sum = 0
    # for i in arr:
    #     sum += abs(i)
    # return sum * product * arr[0]
