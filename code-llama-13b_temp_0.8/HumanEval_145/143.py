
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    # a = [list(map(int, str(i))) for i in nums]
    # # print(a)
    # sums = [sum(i) for i in a]
    # b = sorted(list(enumerate(nums)), key=lambda x: (sums[x[0]], x[1]))
    # result = [i for _, i in sorted(b, key=lambda x: x[0])]
    # return result

    return sorted(nums, key=lambda x: (sum(map(int, str(x))), x))

