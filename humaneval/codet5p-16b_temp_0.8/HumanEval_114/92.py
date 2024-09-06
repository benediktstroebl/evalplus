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

    minSum = math.inf
    sumOfNums = 0
    for num in nums:
        sumOfNums += num
        if sumOfNums < minSum:
            minSum = sumOfNums
        if sumOfNums > 0:
            sumOfNums = 0

    return minSum

