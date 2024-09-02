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
    n = len(nums)
    sum = minNum = nums[0]
    for i in range(1, n):
        sum += nums[i]
        if sum < minNum:
            minNum = sum
        if sum < 0:
            sum = 0
    return minNum
