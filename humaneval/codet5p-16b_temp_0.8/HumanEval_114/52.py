import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i-1]
    minSum = math.inf
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if minSum > nums[j] - nums[i]:
                minSum = nums[j] - nums[i]
    return minSum

