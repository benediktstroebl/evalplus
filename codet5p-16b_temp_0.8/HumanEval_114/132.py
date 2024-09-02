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
    end = 0
    min_sum = math.inf
    total = 0
    while end <= len(nums):
        total += nums[end]
        end += 1
        while total >= nums[start]:
            min_sum = min(total - nums[start], min_sum)
            total -= nums[start]
            start += 1
    return min_sum
