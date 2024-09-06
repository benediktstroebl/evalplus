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
    start, end = 0, 0
    running_sum = 0
    for i in range(len(nums)):
        if running_sum < 0:
            running_sum = 0
            start = i
        running_sum += nums[i]
        end = i
        min_sum = min(min_sum, running_sum)
    return nums[start: end+1]
