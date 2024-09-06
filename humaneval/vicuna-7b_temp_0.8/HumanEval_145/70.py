
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
    def helper(nums, low, high):
        if low >= len(nums):
            return
        if high >= len(nums):
            return
        if (nums[low] + nums[high]) % 10 > (nums[low] + nums[high] // 10) % 10:
            nums[low], nums[high] = nums[high], nums[low]
            helper(nums, low + 1, high - 1)
            helper(nums, low, high)
        else:
            helper(nums, low + 1, high)
    helper(nums, 0, len(nums) - 1)
    return nums