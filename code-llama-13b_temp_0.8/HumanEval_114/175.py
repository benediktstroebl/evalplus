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
    # minSum = math.inf
    sumSoFar = 0
    minSum = nums[0]
    for num in nums:
        sumSoFar += num
        if sumSoFar < minSum:
            minSum = sumSoFar
        if sumSoFar > 0:
            sumSoFar = 0
    return minSum
