
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
    result = 0
    total_prod = 1
    for num in arr:
        total_prod *= num if num else 1
        result += abs(num) if num > 0 else -abs(num)
    return result * total_prod

