
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
    if len(nums) == 0:
        return []

    ret = []
    sum_nums = lambda num: sum([int(i) for i in str(num)])
    for i, num in enumerate(nums):
        ret.append([num, sum_nums(num), i])

    ret.sort(key=lambda x: (x[1], x[2]))

    return [i[0] for i in ret]

