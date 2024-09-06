
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
    if not nums: return []

    result_list = []
    sorted_nums = sorted(nums, key=lambda x: sum(map(int, list(str(x)))))
    sorted_dict = {}

    for num in sorted_nums:
        sorted_dict[sum([int(i) for i in str(num)])] = num
    for num in nums:
        if num in sorted_dict:
            result_list.append(num)
    return result_list

