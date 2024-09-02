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
    if len(nums) == 1:
        return nums[0]

    min_sum = nums[0]
    max_sum = 0
    for i in range(len(nums)):
        max_sum += nums[i]
        if max_sum < 0:
            max_sum = 0
        min_sum = min(min_sum, max_sum)
    return min_sum

