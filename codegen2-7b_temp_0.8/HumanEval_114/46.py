import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    num_sum = 0
    if len(nums) == 0:
        return num_sum
    min_sum = nums[0]
    for i in range(1, len(nums)):
        if num_sum < 0:
            num_sum = nums[i]
        else:
            num_sum += nums[i]
        min_sum = min(min_sum, num_sum)
    return min_
