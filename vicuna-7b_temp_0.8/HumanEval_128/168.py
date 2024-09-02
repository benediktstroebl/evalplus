
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

    signs = [1, -1, 0]
    prod = 1

    for i in range(len(arr)):
        signs = signs[:i+1]
        prod = signs[0]*prod
        arr_product = arr[i]
        arr_product_signs = [1 if a == 1 else -1 if a == -1 else 0 for a in arr_product]
        product_signs = [x if a == 1 else -x if a == -1 else 0 for a, x in zip(arr_product_signs, signs)]
        result = [0] * len(arr_product_signs)
        for j in range(len(product_signs)):
            result[j] = result[j] + product_signs[j] * arr_product_signs[j]
        return result[0] * prod