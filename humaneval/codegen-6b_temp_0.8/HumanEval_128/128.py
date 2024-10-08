
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
        return
    count = {}
    for e in arr:
        if e:
            if e in count:
                count[e] += 1
            else:
                count[e] = 1
    res = 1
    for i in count:
        res *= 1 if count[i] % 2 == 0 else -1
    return res

