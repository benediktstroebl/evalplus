import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = nums[0]
    for i in range(1, len(nums)):
        curr_sum = nums[i]
        for j in range(i + 1, len(nums)):
            curr_sum -= nums[j]
        if curr_sum >= 0:
            min_sum = min(min_sum, curr_sum)
    return min_sum
