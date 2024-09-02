
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
    # if len(arr) == 0, return None
    if len(arr) == 0:
        return None

    # sort the array
    arr = sorted(arr)

    # initialize the sum of magnitudes and product of signs
    sum_of_magnitudes = 0
    product_of_signs = 1
    for num in arr:
        sum_of_magnitudes += abs(num)
        product_of_signs *= (1 if num > 0 else -1) * (1 if num < 0 else 0)

    # return the result
    return sum_of_magnitudes * product_of_signs