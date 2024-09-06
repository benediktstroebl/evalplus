
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
    return sum(arr[0] * (1 if x==1 else -1) * (0 if y==1 else 1) for x, y in zip(arr[1:], arr[0]))

arr = [1, 2, 3, -4, 5]
