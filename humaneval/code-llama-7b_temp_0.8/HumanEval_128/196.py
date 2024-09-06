
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
        return 0

    product_of_signs = 1
    sum_of_numbers = 0

    for n in arr:
        if n > 0:
            product_of_signs = product_of_signs * 1
        elif n < 0:
            product_of_signs = product_of_signs * -1
        else:
            product_of_signs = product_of_signs * 0
        sum_of_numbers += n

    return sum_of_numbers * product_of_signs

