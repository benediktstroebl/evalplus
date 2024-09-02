
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
    signs = [(-1 if n < 0 else 1) for n in arr]
    return sum(abs(reduce(lambda x, y: x * y, signs)) * reduce(lambda x, y: x * y, arr))

    # # Iterate the array
    # for i in range(len(arr)):
    #     if arr[i] != 0:
    #         signs.append(arr[i] / abs(arr[i]))
    #
    # signs = 1 if signs == [] else signs
    # return sum(abs(reduce(lambda x, y: x * y, signs)) * reduce(lambda x, y: x * y, arr))

