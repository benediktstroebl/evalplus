
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

    signs = [1, -1, 0]
    magnitudes = [abs(i) for i in arr]
    result = 0
    for i in range(len(magnitudes)):
        for j in range(i+1, len(magnitudes)):
            sign = signs[j % 3]
            product = magnitudes[i] * magnitudes[j]
            result += sign * product
    return result
