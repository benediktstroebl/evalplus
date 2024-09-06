
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

    # what if there are no numbers?
    if not arr:
        return None

    # some cases for the length of the arr
    # if arr is 1, return the sign of the arr
    if len(arr) == 1:
        return arr[0]
    # if arr is 2, return the first value multiplied by the sign of the second value
    if len(arr) == 2:
        return arr[0] * arr[1]

    # will get the sign of each element and multiply it
    # will then take the absolute value of the product
    sign_product = abs(prod(map(lambda i: i / abs(i), arr)))
    return sign_product * arr[0]

