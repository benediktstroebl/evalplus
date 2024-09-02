import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    subArraySum = math.inf
    i = 0
    for j in range(len(nums)):
        subArraySum = min(subArraySum, sum(nums[i:j+1]))
        if subArraySum < sum(nums[i:j+1]):
            i = j
    return subArraySum
