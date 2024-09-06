
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
    # Solution:
    if len(arr) == 0:
        return None
    
    prod_neg = 1
    prod_pos = 1
    prod_zero = 1
    sum_neg = 0
    sum_pos = 0
    
    for num in arr:
        if num < 0:
            prod_neg *= num
            sum_neg += num
        elif num > 0:
            prod_pos *= num
            sum_pos += num
        else:
            prod_zero *= num
    
    return (prod_neg * prod_pos * prod_zero) + (sum_neg * sum_pos)

    # Time Complexity: O(n)
    # Space Complexity: O(1)

    
