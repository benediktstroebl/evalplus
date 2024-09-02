
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
    if arr:
        fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        return sum([f * abs(i) for i, f in zip(arr, fib)])
    else:
        return None

