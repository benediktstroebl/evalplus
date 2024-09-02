
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
    if not arr: return None
    
    # Consider the following example:
    #  1 x 1 = 1 x 1 x 1 = 1 x 1 x (-1) = -1
    #  We see here that multiplying 1 by 1, 1 by 1 and -1 gives the
    #  same result, so it's enough to count the number of 1's.
    #  The same logic applies to the -1 and 0, since multiplying
    #  by 0 results in 0.
    #  So, we have to count the number of 0's and of -1's, and then
    #  multiply their counts:
    
    count_of_zeroes = arr.count(0)
    count_of_negatives = arr.count(-1)
    result = count_of_zeroes * count_of_negatives

    for num in arr:
        if num > 0:
            result += num
        elif num < 0:
            result -= num
    return result

