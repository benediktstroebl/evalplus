
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
    dict_points = {}
    for i in range(len(nums)):
        sum_i = sum_of_digits(nums[i])
        if sum_i not in dict_points:
            dict_points[sum_i] = [nums[i]]
        else:
            dict_points[sum_i].append(nums[i])

    res = []
    for i in range(len(nums)):
        for key, values in dict_points.items():
            if nums[i] in values:
                res.append(nums[i])

    return res

