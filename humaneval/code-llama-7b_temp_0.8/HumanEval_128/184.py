
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
    result = []
    for i in arr:
        result.append(i if i > 0 else -1 if i < 0 else 0)

    signs = list(map(lambda x: 1 if x > 0 else -1 if x < 0 else 0, result))

    return sum(result) * prod(signs) if signs else None

