import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    start, end = 0, 0
    minLength = math.inf
    currSum = 0
    while end < len(nums):
        currSum += nums[end]
        end += 1
        while currSum >= 0:
            minLength = min(minLength, end - start)
            currSum -= nums[start]
            start += 1

    return minLength if minLength != math.inf else 0
