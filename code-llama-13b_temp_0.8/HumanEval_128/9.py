
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
    # Student's solution
    # product = 1
    # result = 0
    # if arr:
    #     for i in arr:
    #         product *= i
    #     for i in arr:
    #         result += abs(i)*(product // abs(i))
    #     return result
    # return None

    # Solutions from other students
    # import itertools
    # from functools import reduce

    # def sign(num):
    #     if num == 0:
    #         return 0
    #     elif num < 0:
    #         return -1
    #     else:
    #         return 1

    # if not arr:
    #     return None

    # return reduce(lambda x, y: x + y,
    #               map(lambda num: num[0] * num[1],
    #                   zip(arr, itertools.cycle([sign(i) for i in arr]))))

    # def sign(num):
    #     return num and (num // abs(num))

    # if len(arr) == 0:
    #     return None

    # # defaultdict would be handy here
    # signs = {
    #     1: 1,
    #     -1: 1,
    #     0: 0
    # }

    # for num in arr:
    #     signs[sign(num)] *= abs(num)

    # return sum(abs(num) * signs[sign(num)] for num in arr)

    if len(arr) < 1:
        return None

    product = 1
    for i in arr:
        product *= i

    return sum(abs(i)*(product // abs(i)) for i in arr)

