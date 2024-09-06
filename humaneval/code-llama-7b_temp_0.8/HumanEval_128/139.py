
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
    # print(arr)
    if len(arr) == 0:
        return None

    arr = [int(i) for i in arr]
    arr.sort(key = abs)
    # print(arr)
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = 1
    # print(arr)
    # print(sum([i*arr[i] for i in range(len(arr))]))
    # print(arr[::-1])
    # print([arr[i]*arr[i] for i in range(len(arr))])
    # print([arr[i]*arr[i] for i in range(len(arr))][::-1])
    # print(sum([arr[i]*arr[i] for i in range(len(arr))][::-1]))
    return sum([arr[i]*arr[i] for i in range(len(arr))])*prod([arr[i] for i in range(len(arr))])

