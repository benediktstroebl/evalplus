
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

    # initialize result
    result = 0

    # loop through array and calculate product of signs of each number
    for i in range(len(arr)):
        sign1 = 1 if arr[i] > 0 else -1
        sign2 = 1 if arr[i] > 0 else -1
        sign3 = 1 if arr[i] > 0 else -1
        result *= (sign1 * sign2 * sign3)

    # store the result
    return result