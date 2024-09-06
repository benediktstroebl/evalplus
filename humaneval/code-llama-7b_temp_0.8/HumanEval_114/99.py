import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    currMin = minSum = nums[0]

    for num in nums[1:]:
        currMin = min(currMin + num, num)
        minSum = min(minSum, currMin)

    return minSum
