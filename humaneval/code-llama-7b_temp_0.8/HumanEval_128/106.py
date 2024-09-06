
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
    # if len(arr) == 0:
    #     return None
    # arr_1 = arr
    # arr_1 = [i*1 for i in arr]
    # arr_2 = arr
    # arr_2 = [i*-1 for i in arr]
    # arr_3 = arr
    # arr_3 = [i*0 for i in arr]
    # print(arr_1)
    # print(arr_2)
    # print(arr_3)
    # return sum([arr_1[i]*arr_2[i]*arr_3[i] for i in range(len(arr))])
    # print(sum([arr_1[i]*arr_2[i]*arr_3[i] for i in range(len(arr))]))
    if len(arr) == 0:
        return None
    prod = 1
    signs = []
    for num in arr:
        prod = prod * (num / abs(num))
        signs.append(num / abs(num))
    return sum([i * prod for i in signs])

