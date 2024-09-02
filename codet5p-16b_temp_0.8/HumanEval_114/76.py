import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    n = len(nums)
    
    if n == 1:
        return nums[0]
    
    curr_sum = math.inf
    
    for i in range(n):
        
        curr_sum = min(curr_sum, nums[i] + minSubArraySum(nums[i+1:]))
    
    return curr_sum
    
