
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
    arr = [i for i in arr if i != 0]
    if len(arr) == 0:
        return None
    return sum(map(lambda x: x * sign(arr[0]), (arr[0],) + (sign(arr[i]) if i != 0 else (1,)) for i in range(len(arr)) if i != 0))