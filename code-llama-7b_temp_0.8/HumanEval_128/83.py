
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
    # 2.867s
    # return sum(map(abs, arr)) * (1 * math.prod(map(lambda x: -1 if x < 0 else 1, arr)))

    # 3.069s
    # res = 0
    # for elem in arr:
    #     res += abs(elem)
    #     if elem < 0:
    #         res *= -1
    # return res

    # 3.153s
    # return 0 if arr == [] else sum(abs(x) for x in arr) * (-1 if min(arr) < 0 else 1)

    # 2.668s
    # return 0 if arr == [] else sum(abs(x) for x in arr) * (-1 if any(x < 0 for x in arr) else 1)

    # 2.635s
    # return 0 if not arr else sum(abs(x) for x in arr) * (-1 if arr[0] < 0 else 1)

    # 2.949s
    # return 0 if not arr else sum(abs(x) for x in arr) * (-1 if any(x < 0 for x in arr) else 1)

    # 2.880s
    # return 0 if arr == [] else sum(abs(x) for x in arr) * (-1 if min(arr) < 0 else 1)

    # 3.244s
    # return 0 if arr == [] else sum(abs(x) for x in arr) * (-1 if min(map(lambda x: -1 if x < 0 else 1, arr)) else 1)

    # 2.721s
    # return 0 if arr == [] else sum(abs(x) for x in arr) * (-1 if min(map(lambda x: 1 if x < 0 else -1, arr)) else 1)

    # 2.938s
    # return 0 if arr == [] else sum(abs(x) for x in arr) * (-1 if
