
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
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return abs(arr[0] * arr[1]) * (arr[0] // arr[1] or arr[1] // arr[0] or 1)

    first_magnitude = abs(arr[0])
    first_sign = 1 if arr[0] > 0 else -1 if arr[0] < 0 else 0
    signs_product = 1
    for i in range(1, len(arr)):
        if arr[i] > 0:
            signs_product *= -1
        if arr[i] < 0:
            signs_product *= -1
        if arr[i] == 0:
            return 0
        first_magnitude *= abs(arr[i])

    return first_magnitude * first_sign * signs_product
