
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
    sorted_list = []
    for i in nums:
        sorted_list.append(get_points(i))
    sorted_list, result = sorted(sorted_list), []
    for i in range(len(sorted_list)):
        result.append(nums[sorted_list.index(sorted_list[i])])
    return result

