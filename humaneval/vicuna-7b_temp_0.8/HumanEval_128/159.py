
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
    for i in range(len(arr)):
        if arr[i] != 0:
            sign = 1
        else:
            sign = 0
            for j in range(i, len(arr)):
                if arr[j] != 0:
                    sign *= -1
            if arr[i] != 0:
                sign *= -1
            for j in range(i, len(arr)):
                sign *= arr[j]
            if arr[i] != 0:
                sign *= -1
        return sign
