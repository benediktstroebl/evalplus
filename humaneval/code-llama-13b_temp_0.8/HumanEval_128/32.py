
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
    # return None for empty arr
    if len(arr) == 0:
        return None

    # To get the signs of each number in the array
    signs = [i // abs(i) for i in arr]
    # To get the product of signs of each number in the array
    signs_product = 1
    for i in range(len(signs)):
        signs_product = signs_product * signs[i]

    # To get the magnitudes of integers of each number in the array
    magnitudes = [abs(i) for i in arr]
    # To get the sum of magnitudes of integers of each number in the array
    magnitude_sum = sum(magnitudes)

    return magnitude_sum * signs_product

