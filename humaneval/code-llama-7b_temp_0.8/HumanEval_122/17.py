
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    # import math
    # return sum([x for x in arr[:k] if math.log10(x) <= 2])

    # import functools
    # return sum(list(filter(lambda x: functools.reduce(lambda acc, x: acc + x, list(map(lambda x: int(x), str(x)))), arr[:k])))

    # return sum(map(lambda x: x, filter(lambda x: x <= 99, arr[:k])))

    # return sum(arr[:k]) - sum(filter(lambda x: x > 99, arr[:k]))

    # return sum(arr[:k]) - sum(filter(lambda x: x > 99, arr[:k]))
    # # another solution
    #
    # return sum(arr[:k]) - sum(x for x in arr[:k] if x > 99)

    # return sum(arr[:k]) - sum(x for x in arr[:k] if x > 99)

    # return sum(arr[:k]) - sum(x for x in arr[:k] if len(str(x)) > 2)

    # return sum(arr[:k]) - sum(x for x in arr[:k] if int(len(str(x))) > 2)

    # return sum(arr[:k]) - sum(x for x in arr[:k] if len(str(x)) > 2)

    # import itertools
    # return sum(arr[:k]) - sum(itertools.chain.from_iterable([x for x in arr[:k] if len(str(x)) > 2]))

    # return sum(arr[:k]) - sum(x for x in arr[:k] if len(str(x)) > 2)

    # return sum(arr[:k]) - sum(x for x in arr[:k] if len(str(x)) > 2)

    # return sum(arr[:k]) - sum([x for x in arr[:k] if len(str(x)) > 2])

    # return sum(arr[:k]) - sum([x for x in arr[:k
