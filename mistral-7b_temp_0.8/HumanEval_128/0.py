
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
    #iterate through the array
    sign=1
    sum=0
    for i in arr:
        #if i is zero
        if i==0:
            return None
        #if i is positive
        elif i>0:
            sign=1
        #if i is negative
        elif i<0:
            sign=-1
        sum+=i*sign
    return sum
