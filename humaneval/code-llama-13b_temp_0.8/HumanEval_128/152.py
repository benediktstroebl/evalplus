
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
    return (arr[0] and 1) * sum([(arr[i] and 1) for i in range(1, len(arr))]) * sum(
        [
            (arr[i] or -1) * (arr[i - 1] or -1) * (arr[i - 2] or -1)
            for i in range(2, len(arr))
        ]
    )

