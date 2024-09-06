
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

    positive_num = 0
    negative_num = 0
    for i in arr:
        if i > 0:
            positive_num += 1
        elif i < 0:
            negative_num += 1

    result = 0
    if positive_num == 0:
        result = negative_num * arr[0]
    elif negative_num == 0:
        result = positive_num * arr[0]
    else:
        result = (positive_num - negative_num) * arr[0]

    return result

