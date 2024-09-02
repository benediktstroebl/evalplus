import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 0:
        return 0

    maxSum = nums[0]
    minSum = nums[0]

    for i in range(1, len(nums)):
        if maxSum < 0:
            maxSum = nums[i]
        elif maxSum + nums[i] > 0:
            maxSum += nums[i]
        else:
            maxSum = 0

        if minSum > 0:
            minSum += nums[i]
        elif minSum + nums[i] < 0:
            minSum = nums[i]
        else:
            minSum = 0

    if minSum == 0:
        return maxSum
    else:
        return minSum
