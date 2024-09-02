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
        start = max(0, i)
        end = min(i, len(nums) - 1)
        sum = start + (nums[end] - nums[start])
        if sum < min_sum:
            min_sum = sum
        elif sum == min_sum and nums[start] > nums[end]:
            min_sum = sum
    return min_sum
