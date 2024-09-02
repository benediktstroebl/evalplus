import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    min_sum = nums[0]
    window_sum = nums[0]

    for num in nums[1:]:
        window_sum += num
        min_sum = min(min_sum, window_sum)
        window_sum = max(window_sum, 0)

    return min(min_sum, window_sum)
