
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
    # Client Data Validation
    if not isinstance(arr, list):
        raise TypeError(f"Argument should be a list but it is {arr}")

    # App-layer Data Validation
    if not arr:
        return None

    # Sol
    pos_prod = 1
    neg_prod = 1
    sign_sum = 0
    for num in arr:
        if num == 0:
            continue
        sign_sum += (num > 0) - (num < 0)
        pos_prod *= max(num, 1)
        neg_prod *= min(num, 0)
    return (pos_prod - neg_prod) * sign_sum

