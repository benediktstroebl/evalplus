
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
    if len(arr) == 0:
        return None

    negative = 0
    zero = 0
    positive = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zero += 1
        if arr[i] < 0:
            negative += 1
        if arr[i] > 0:
            positive += 1

    if negative % 2 == 0 and positive % 2 == 0:
        return arr[0] * zero
    elif negative % 2 == 0 and positive % 2 == 1:
        return arr[0] * zero * -1
    elif negative % 2 == 1 and positive % 2 == 1:
        return arr[0] * zero
    elif negative % 2 == 1 and positive % 2 == 0:
        return arr[0] * zero * -1

