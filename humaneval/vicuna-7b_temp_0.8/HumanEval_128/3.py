
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
    if not arr:
        return None
    
    # sort the array
    arr = sorted(arr)
    
    # calculate the product of signs
    prod_sign = 1
    for i in range(len(arr)):
        if arr[i] == 1:
            prod_sign *= -1
        elif arr[i] == -1:
            prod_sign *= 1
        else:
            prod_sign *= 0
    
    # calculate the sum of magnitudes
    sum_magnitude = 0
    for i in range(len(arr)):
        sum_magnitude += abs(arr[i])
    
    # calculate the product of magnitudes
    prod_magnitude = 1
    for i in range(len(arr)):
        prod_magnitude *= abs(arr[i])
    
    # calculate the result
    result = 0
    for i in range(len(arr)):
        result += sum_magnitude * prod_sign * prod_magnitude * arr[i]
    
    return result