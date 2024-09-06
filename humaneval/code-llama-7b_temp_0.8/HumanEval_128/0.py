
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
    # result, i = 0, 0
    # while i < len(arr):
    #     if arr[i] != 0:
    #         result += abs(arr[i])
    #         if arr[i] > 0:
    #             arr[i] = 1
    #         else:
    #             arr[i] = -1
    #     else:
    #         arr[i] = 0
    #     i += 1
    # return None if len(arr) == 0 else result * prod(arr)
    return None if len(arr) == 0 else sum([abs(i) for i in arr]) * prod([1 if i > 0 else -1 if i < 0 else 0 for i in arr])

