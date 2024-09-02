
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
    res = []
    while nums:
        max_num, max_num_index = 0, 0
        for i, num in enumerate(nums):
            if max_num < sum([int(x) for x in str(num)]) \
                and num >= 0:
                max_num, max_num_index = sum([int(x) for x in str(num)]), i
        if max_num < 0:
            max_num, max_num_index = max_num, max_num_index
        res.append(nums.pop(max_num_index))
    return res

