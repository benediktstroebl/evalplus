
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
    if len(arr) == 0:
        return None
    else:
        positive_arr = []
        negative_arr = []
        zero_arr = []
        for num in arr:
            if num > 0:
                positive_arr.append(num)
            elif num < 0:
                negative_arr.append(num)
            else:
                zero_arr.append(num)
        return sum(positive_arr) * sum(negative_arr) * sum(zero_arr)

