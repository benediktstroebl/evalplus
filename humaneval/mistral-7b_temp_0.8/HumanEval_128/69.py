
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
    elif len(arr) == 1:
        return abs(arr[0])
    else:
        left_prod = 1
        right_prod = 1
        left_signs = 0
        right_signs = 0
        for i in range(len(arr) // 2):
            if arr[i] < 0:
                left_prod *= arr[i]
                left_signs += 1
            if arr[len(arr) - 1 - i] < 0:
                right_prod *= arr[len(arr) - 1 - i]
                right_signs += 1
        return (left_signs + 1) * (right_signs + 1) * abs(left_prod * right_prod)
