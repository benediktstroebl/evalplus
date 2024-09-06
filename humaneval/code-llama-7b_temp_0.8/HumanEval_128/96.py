
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
    if arr == []:
        return None
    else:
        signs = list(map(lambda x: (x > 0) - (x < 0), arr))
        signs_product = 1
        for num in signs:
            signs_product *= num
        result = 0
        for num in arr:
            if num == 0:
                continue
            else:
                result += abs(num) * signs_product
        return result

