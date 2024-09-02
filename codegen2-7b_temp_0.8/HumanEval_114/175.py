import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    total = sum(nums)
    l = 0
    r = total
    min_sum = math.inf
    while l < r:
        if sum(nums[l:r+1]) < min_sum:
            min_sum = sum(nums[l:r+1])
        if sum(nums[l:r]) < min_sum:
            min_sum = sum(nums[l:r])
        
