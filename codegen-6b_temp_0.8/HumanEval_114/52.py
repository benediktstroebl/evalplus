import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    n = len(nums)
    min_sum = math.inf
    min_sub = []
    for i in range(n):
        if i == 0:
            min_sum = nums[i]
            min_sub.append(nums[i])
        else:
            min_sum = min(nums[i], min_sum + nums[i])
            min_sub.append(min_sum)
    return min_sub
