
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
    if nums == []:
        return nums
    elif nums == [None]:
        return nums
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums.pop(i+1)
    return nums
