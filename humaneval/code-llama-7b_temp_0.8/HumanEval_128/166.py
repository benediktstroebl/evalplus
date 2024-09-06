
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
    # 1. check that the array is not empty.
    if len(arr) == 0:
        return None
    # 2. initialize the sign and the result.
    result = 1
    sign = 1
    # 3. iterate through the numbers in the array.
    for number in arr:
        # 4. check if the number is negative.
        if number < 0:
            # 5. update the sign
            sign = -1
        # 6. update the result
        result *= sign
        # 7. reset the sign
        sign = 1
    # 8. multiply result by the product of the signs of each number
    return result * sum([abs(number) for number in arr])

