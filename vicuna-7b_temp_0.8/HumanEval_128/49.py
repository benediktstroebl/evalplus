
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

    sums = [sum(arr) for _ in range(len(arr))]
    prod = [sum(map(abs, arr)) for _ in range(len(arr))]
    result = [0] * len(arr)

    for i in range(1, len(arr)):
        if arr[i] == -1:
            result[i] *= prod[i-1]
        elif arr[i] == 1:
            result[i] *= prod[i]
        else:
            result[i] *= prod[i] * (prod[i] % 2 == 0)

    return sum(result)