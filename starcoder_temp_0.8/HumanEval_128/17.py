
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

    def prod_signs_helper(arr, i):
        if i == len(arr):
            return 1

        result = prod_signs_helper(arr, i + 1)
        if arr[i] == 0:
            return result
        if arr[i] < 0:
            result *= -1

        return result * arr[i]

    if len(arr) == 0:
        return None

    return prod_signs_helper(arr, 0) * sum(map(abs, arr))
