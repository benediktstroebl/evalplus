import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = math.inf
    for i in range(len(nums)):
        for j in range(i):
            sum = nums[i] + nums[j]
            if sum < min_sum:
                min_sum = sum
    return min_sum

nums = [3, 2, 2, 1, 1, 1, 1]
