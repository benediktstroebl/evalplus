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
        return math.inf
    if len(nums) == 1:
        return nums[0]
    minSum = nums[0]
    for index, num in enumerate(nums[1:]):
        minSum += num
        if minSum < nums[index]:
            minSum = nums[index]
    return minSum
