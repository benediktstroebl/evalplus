
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
    # Step 1: return None for empty arr.
    if not arr:
        return None
    # Step 2: initialize sign_product and sum_magnitude.
    sign_product, sum_magnitude = 1, 0
    # Step 3: iterate over array.
    for n in arr:
        if n:
            sign_product *= (-1) ** (n < 0)
            sum_magnitude += abs(n)
    # Step 4: return result.
    return sign_product * sum_magnitude
