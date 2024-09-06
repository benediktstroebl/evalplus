
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
    # def sum_of_digits(num):
    #     res = 0
    #     for i in str(num):
    #         res += int(i)
    #     return res
    #
    # res = []
    # for i in nums:
    #     res.append((sum_of_digits(i), i))
    # res.sort()
    #
    # return [i[1] for i in res]

    res = sorted(nums, key = lambda x: (sum(map(int, str(x))), x))

    return res
