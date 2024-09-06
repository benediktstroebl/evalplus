
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
    if arr == []:
        return None
    elif len(arr) == 1:
        if arr[0] == 0:
            return 0
        else:
            return arr[0]
    else:
        prod = 1
        for i in arr:
            prod = prod * i

        signs_list = []
        for i in range(len(arr)):
            if arr[i] < 0:
                signs_list.append(-1)
            elif arr[i] > 0:
                signs_list.append(1)
            else:
                signs_list.append(0)

        sum_signs = 0
        for i in range(len(signs_list)):
            sum_signs = sum_signs + signs_list[i] * arr[i]

        return sum_signs * prod

