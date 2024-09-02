
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
    # sort the array in descending order
    arr = sorted(arr, reverse=True)

    # initialize the product of signs for each number
    sign_prod = [[1, -1, 0] for _ in range(len(arr))]

    # initialize the sum of magnitudes
    magnitude = 0

    # loop through the array
    for i in range(len(arr)):
        # get the current magnitude
        mag = abs(arr[i])

        # get the current sign
        sign = arr[i]

        # update the sign product for the current magnitude
        sign_prod[i][sign] *= mag

        # update the sum of magnitudes
        magnitude += mag

    # return the sum of magnitudes multiplied by the product of signs
    return magnitude * sum(sign_prod)