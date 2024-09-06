
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

    sum_of_magnitudes = 0

    for number in arr:
        magnitude = abs(number)
        sum_of_magnitudes += magnitude

    if len(arr) == 0:
        return None

    prod = 1
    for number in arr:
        prod *= number / abs(number)

    return sum_of_magnitudes * prod

