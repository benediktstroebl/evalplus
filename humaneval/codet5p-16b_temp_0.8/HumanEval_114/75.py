import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if nums is None or len(nums) == 0:
        return math.inf
    summ = 0
    minSum = math.inf
    for i in range(len(nums)):
        summ += nums[i]
        minSum = min(minSum, summ)
        if summ < 0:
            summ = 0
    return minSum

