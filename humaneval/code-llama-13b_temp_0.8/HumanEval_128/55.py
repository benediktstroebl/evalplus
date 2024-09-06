
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
    # Solution 1
    if not arr:
        return None

    signs = [arr[0]] * len(arr)
    for index in range(1, len(arr)):
        signs[index] = signs[index-1] * arr[index]

    return sum(abs(arr[index]) * signs[index] for index in range(len(arr)))


    # Solution 2
    if not arr:
        return None

    signs = [arr[0]] * len(arr)
    for index in range(1, len(arr)):
        signs[index] = signs[index-1] * arr[index]

    return sum(abs(arr[index]) * signs[index] for index in range(len(arr)))


    # Solution 3
    if not arr:
        return None

    signs = [arr[0]] * len(arr)
    for index in range(1, len(arr)):
        signs[index] = signs[index-1] * arr[index]

    return sum(abs(arr[index]) * signs[index] for index in range(len(arr)))
