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

    max_sum = nums[0]
    min_sum = nums[0]
    for i in range(1, len(nums)):
        max_sum = max(max_sum + nums[i], nums[i])
        min_sum = min(min_sum + nums[i], nums[i])
    
    return min_sum
