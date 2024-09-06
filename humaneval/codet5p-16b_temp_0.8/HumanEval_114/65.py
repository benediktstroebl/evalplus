import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    s = sum(nums)
    
    if s <= 0:
        return math.inf
    
    min_subarr_sum = math.inf
    l, r = 0, 0
    while r < len(nums):
        curr_sum = sum(nums[l:r+1])
        min_subarr_sum = min(min_subarr_sum, curr_sum)
        if curr_sum < s:
            r += 1
        else:
            l += 1
    
    return min_subarr_sum
    
    
