
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
    # check if empty array
    if not arr:
        return None

    # create a dictionary to store the sign of each number
    signs = {}
    for num in arr:
        if num in signs:
            signs[num] = -1 * signs[num]
        else:
            signs[num] = 1

    # create a list to store the sum of magnitudes
    sum_list = [abs(num) for num in arr]

    # calculate the sum of magnitudes and product of signs
    magnitude_sum = sum(sum_list)
    product = 0
    for num, sign in signs.items():
        if num not in signs:
            product *= sign
        else:
            product *= sign * signs[num]
    product = abs(product)

    # return the result
    return magnitude_sum * product