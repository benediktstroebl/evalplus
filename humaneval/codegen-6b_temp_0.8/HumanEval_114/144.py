import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    minSum = nums[0]
    subSum = 0
    i = 0
    for num in nums:
        subSum += num
        if minSum > subSum:
            minSum = subSum
        if subSum < 0:
            subSum = 0
        i += 1
    return minSum
    

