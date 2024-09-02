import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    start = 0
    minSubArray = math.inf
    # sum = nums[0]
    subArraySum = nums[0]
    minSum = nums[0]

    for end in range(len(nums)):
        subArraySum += nums[end]
        while subArraySum > minSum:
            subArraySum -= nums[start]
            start += 1
        if minSubArray > subArraySum:
            minSubArray = subArraySum
            minSum = subArraySum
    return minSum




