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
    for i in range(1, n):
        for j in range(i):
            for k in range(i+1, n):
                if nums[i] + nums[j] + nums[k] == nums[i]+nums[j]:
                    return nums[i] + nums[j]
    return 0
