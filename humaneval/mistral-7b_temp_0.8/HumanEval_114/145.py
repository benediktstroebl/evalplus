import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) <= 1:
        return nums[0]

    minSum = 10000000000000
    for i in range(len(nums)):
        sum = nums[i]
        for j in range(i+1,len(nums)):
            sum += nums[j]
            if sum < minSum:
                minSum = sum
    return minSum
