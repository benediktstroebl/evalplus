import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    sums = sum(nums)
    best = math.inf
    
    for i in range(len(nums)):
        if sum(nums[i:]) < best:
            best = sum(nums[i:])
            
    return best
