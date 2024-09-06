
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
    sign=1
    if arr:
        for i in arr:
            if i==0:
                return None
            elif i>0:
                sign*=i
            else:
                sign*=i*(-1)
        return abs(sign)
    else:
        return None

