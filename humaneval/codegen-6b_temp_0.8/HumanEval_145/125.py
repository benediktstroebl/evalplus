
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
    from collections import OrderedDict
    nums_dict = OrderedDict()
    for num in nums:
        sum_of_digits = sum(map(int, str(num)))
        if sum_of_digits not in nums_dict:
            nums_dict[sum_of_digits] = [num]
        else:
            nums_dict[sum_of_digits].append(num)
    return [nums_dict.popitem()[0] for nums_dict in nums_dict.values()][::-1]

