
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
    # your code here

    signs = [1, -1, 0]
    mult = 1
    sum_of_mag = 0

    if len(arr) == 0:
        return None
    for i in arr:
        if i != 0:
            sum_of_mag += abs(i)
            mult *= signs[i//abs(i)]

    return sum_of_mag * mult

