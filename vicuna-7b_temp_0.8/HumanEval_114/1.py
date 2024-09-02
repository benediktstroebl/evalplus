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
        if nums[i] == 0:
            min_sum += nums[i]
            continue
        for j in range(i):
            min_sum -= nums[j]
        min_sum -= nums[i]
    return min_sum

nums = [1, 2, 3, 4, 5, 2, 1, 3, 4, 1]
result = minSubArraySum(nums)
