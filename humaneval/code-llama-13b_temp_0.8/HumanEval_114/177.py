import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = math.inf
    i = 0

    while i < len(nums):
        j = i
        subArraySum = 0

        while j < len(nums):
            subArraySum += nums[j]
            j += 1

            if subArraySum < minSum:
                minSum = subArraySum

        i += 1

    return minSum

