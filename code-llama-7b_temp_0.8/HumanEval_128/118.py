
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
    # your code here
    if arr == []:
        return None
    sign_arr = []
    result = 0
    for i in arr:
        if i == 0:
            sign_arr.append(0)
            result = result + 0
        elif i > 0:
            sign_arr.append(1)
            result = result + 1
        else:
            sign_arr.append(-1)
            result = result - 1

    result = result * (abs(sign_arr.count(1)) * abs(sign_arr.count(-1)))
    return result

