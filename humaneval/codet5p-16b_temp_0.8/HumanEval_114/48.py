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
    currentSum = 0
    minSum = math.inf
    left = 0
    for i in range(len(nums)):
        currentSum += nums[i]
        while currentSum >= minSum:
            minSum = min(minSum, currentSum - minSum + nums[left])
            currentSum -= nums[left]
            left += 1
    return minSum
