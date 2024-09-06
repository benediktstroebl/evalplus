
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
    def calc_magnitude(sign):
        if sign == 0:
            return 0
        elif sign == 1:
            return 1
        else:
            return -1

    def calc_mags(arr):
        if arr == []:
            return None
        else:
            return calc_magnitude(arr[0]) * calc_mags(arr[1:])

    return calc_mags(arr)

