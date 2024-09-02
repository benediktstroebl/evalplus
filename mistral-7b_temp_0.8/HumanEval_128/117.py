
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
    """
    :type arr: list of int
    :rtype: int
    """
    if len(arr) == 0:
        return None

    positive = 0
    negative = 0
    zero = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
        else:
            zero += 1

    if positive == 0 and negative == 0:
        return 0
    elif positive == 0 and negative == 1:
        return arr[zero]
    elif positive == 1 and negative == 0:
        return -arr[zero]
    else:
        return arr[zero] * (positive ** negative)

