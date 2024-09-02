
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
    # check if arr is empty
    if arr == []:
        return None
    # make a copy of arr so we don't modify original arr
    arr_copy = arr.copy()
    # define sign function
    def sign(n):
        if n > 0:
            return 1
        elif n < 0:
            return -1
        else:
            return 0
    # define a variable to hold sum of signs
    sum_sign = 0
    # define a variable to hold product of all signs
    product_sign = 1
    # loop over arr_copy
    for n in arr_copy:
        # add the sign of each number to sum_sign
        sum_sign += sign(n)
        # multiply the sign of each number to product_sign
        product_sign *= sign(n)
    # return sum_sign * product_sign
    return sum_sign * product_sign







