import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    start = 0
    minimum = nums[0]
    while start < len(nums) - 1:
        end = start + 1
        current_sum = nums[start]
        while end < len(nums):
            current_sum += nums[end]
            if current_sum < minimum:
                minimum = current_sum
            end += 1
        start += 1
    return minimum
