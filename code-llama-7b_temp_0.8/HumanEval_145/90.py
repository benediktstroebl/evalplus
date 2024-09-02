
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
    nums_dict = {}
    for i in range(len(nums)):
        num_str = str(nums[i])
        total = 0
        for digit in num_str:
            total += int(digit)
        nums_dict[nums[i]] = total
    return sorted(nums_dict, key = lambda x: (nums_dict[x], x))
