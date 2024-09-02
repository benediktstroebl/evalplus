import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if nums:
        currentSum = nums[0]
        minSum = nums[0]
        for i in range(1, len(nums)):
            currentSum = currentSum + nums[i]
            minSum = min(minSum, currentSum)
            currentSum = max(0, currentSum)

        return minSum

    else:
        return 0
