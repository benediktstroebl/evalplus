
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
    if arr == []:
        return None
    else:
        arr = arr[:]
        arr.sort()
        ans = []
        for i in arr:
            ans.append(abs(i))
        return abs(arr[0] * arr[1] * arr[2] * arr[3] * ans[0] * ans[1] * ans[2] * ans[3])

