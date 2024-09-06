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
    if n == 0:
        return 0
    result = nums[0]
    for i in range(1, n):
        for j in range(i, n):
            if nums[i] + nums[j] < nums[i]:
                result += nums[i] + nums[j]
        else:
            result += nums[i]
    return result
