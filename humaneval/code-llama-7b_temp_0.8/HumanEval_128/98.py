
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

    negs = [el for el in arr if el < 0]
    neg_num = len(negs)
    pos_num = len(arr) - neg_num

    if neg_num % 2 == 0:
        return pos_num * neg_num * sum(arr)
    return pos_num * neg_num * sum(map(lambda x: -x, arr))

