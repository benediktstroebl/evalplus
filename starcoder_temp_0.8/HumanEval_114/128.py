import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 0:
        return 0
    summ = [0]*len(nums)
    summ[0] = nums[0]
    for i in range(1, len(nums)):
        summ[i] = summ[i-1] + nums[i]
    m = float('inf')
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            m = min(summ[j] - summ[i], m)
    return m
